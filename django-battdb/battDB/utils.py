from django.core.exceptions import ValidationError
from galvanalyser.harvester.parsers.biologic_parser import BiologicCSVnTSVParser
from galvanalyser.harvester.parsers.maccor_parser import MaccorXLSParser
from galvanalyser.harvester.parsers.parser import Parser
import pandas.errors

class DummyParser(Parser):
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def get_metadata(self):
        return ({'num_rows': 0}, {})

    def get_data_generator_for_columns(self, columns=[], first_data_row=0, col_mapping={}):
        return []


def get_parser(instance):
    # print("result_post_save: Sender: %s, Instance: %s, args: %s, kwargs: %s, base_loc: %s, Filename: %s" % (
    #     sender, instance, args, kwargs, instance.raw_data_file.file.storage.base_location, instance.raw_data_file.file.name))

    filepath = "/".join([instance.raw_data_file.file.storage.base_location, instance.raw_data_file.file.name])
    # TODO: Work out which type of file it is and call the correct parser!
    # parser = BiologicCSVnTSVParser(filepath)

    file_format = instance.use_parser.file_format

    if file_format == "biologic":
        parser = BiologicCSVnTSVParser(filepath)
    elif file_format == "maccor":
        parser = MaccorXLSParser(filepath)
    else:
        parser = DummyParser(filepath)
    return parser

# When saving a data file, call this to parse the data.
def parse_data_file(instance, file_format="csv", columns=['time/s', 'Ecell/V', 'I/mA']):
    if not instance:
        return
    if hasattr(instance, '_dirty'):
        return

    try:
        parser = get_parser(instance)
        (instance.parsed_metadata, cols) = (parser.get_metadata())
    except (pandas.errors.ParserError, ValueError) as e:
        print(e)
        raise ValidationError(message={'raw_data_file': "File parsing failed: " + str(e)})

    all_columns = [k for k in cols.keys()]
    instance.attributes['file_columns'] = all_columns
    parse_columns = [c for c in columns if c in all_columns]
    instance.attributes['parsed_columns'] = parse_columns
    missing_columns = [c for c in columns if c not in all_columns]
    instance.attributes['missing_columns'] = missing_columns
    total_rows = instance.parsed_metadata.get('num_rows') or 0
    instance.attributes['file_rows'] = total_rows
    instance.attributes['range_config'] = {'all':{'start':1, 'end':total_rows,'action': 'all'}}
    # instance.parsed_data = [None] * instance.attributes['num_rows']


    # save again after setting metadata but don't get into a recursion loop!
    try:
        instance._dirty = True
        instance.save()
    finally:
        del instance._dirty
        return parser
