import pandas.errors
from django.core.exceptions import ValidationError

from galvanalyser.harvester import battery_exceptions, maccor_functions
from galvanalyser.harvester.parsers.biologic_parser import BiologicCSVnTSVParser
from galvanalyser.harvester.parsers.maccor_parser import MaccorXLSParser
from galvanalyser.harvester.parsers.parser import Parser


def identify_file(file_path):
    """
    Returns a string identifying the type of the input file
    """
    try:
        if file_path.endswith(".xls"):
            return {"EXCEL", "MACCOR"}
        elif file_path.endswith(".xlsx"):
            return {"EXCEL", "MACCOR"}
        elif file_path.endswith(".csv"):
            if maccor_functions.is_maccor_text_file(file_path, ","):
                return {"CSV", "MACCOR"}
            elif maccor_functions.is_maccor_text_file(file_path, "\t"):
                return {"TSV", "MACCOR"}
        elif file_path.endswith(".txt"):
            if file_path.endswith(".mps.txt"):
                # Bio-Logic settings file, doesn't contain data
                pass
            elif file_path.endswith(".mps.txt"):
                # Bio-Logic text data file
                pass
            elif maccor_functions.is_maccor_text_file(file_path, "\t"):
                return {"TSV", "MACCOR"}
        else:
            # No extension or unrecognised extension
            if maccor_functions.is_maccor_raw_file(file_path):
                return {"RAW", "MACCOR"}
    except Exception as ex:
        print("Error identifying file: " + file_path)
        print(ex)
    raise battery_exceptions.UnsupportedFileTypeError


class DummyParser(Parser):
    def __init__(self, file_path: str) -> None:
        super(DummyParser, self).__init__(file_path)
        self.file_path = file_path

    def get_metadata(self):
        return ({"num_rows": 0}, {})

    def get_data_generator_for_columns(
        self, columns=[], first_data_row=0, col_mapping={}
    ):
        return []


def get_parser(instance):

    filepath = "/".join(
        [
            instance.raw_data_file.file.storage.base_location,
            instance.raw_data_file.file.name,
        ]
    )

    file_format = instance.use_parser.file_format

    if file_format == "biologic":
        parser = BiologicCSVnTSVParser(filepath)
    elif file_format == "maccor":
        parser = MaccorXLSParser(filepath)
    else:
        parser = DummyParser(filepath)
    return parser


# When saving a data file, call this to parse the data.
def parse_data_file(instance, file_format="csv", columns=("time/s", "Ecell/V", "I/mA")):
    if not instance:
        return
    if hasattr(instance, "_dirty"):
        return

    try:
        parser = get_parser(instance)
        (instance.parsed_metadata, cols) = parser.get_metadata()
    except (pandas.errors.ParserError, ValueError) as e:
        print(e)
        raise ValidationError(
            message={"raw_data_file": "File parsing failed: " + str(e)}
        )

    all_columns = [k for k in cols.keys()]
    instance.attributes["file_columns"] = all_columns
    parse_columns = [c for c in columns if c in all_columns]
    instance.attributes["parsed_columns"] = parse_columns
    missing_columns = [c for c in columns if c not in all_columns]
    instance.attributes["missing_columns"] = missing_columns
    total_rows = instance.parsed_metadata.get("num_rows") or 0
    instance.attributes["file_rows"] = total_rows
    instance.attributes["range_config"] = {
        "all": {"start": 1, "end": total_rows, "action": "all"}
    }

    # save again after setting metadata but don't get into a recursion loop!
    try:
        instance._dirty = True
        instance.save()
    finally:
        del instance._dirty
        return parser
