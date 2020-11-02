from django.core.exceptions import ValidationError
from galvanalyser.harvester.parsers.biologic_parser import BiologicCSVnTSVParser
from galvanalyser.harvester.parsers.maccor_parser import MaccorXLSParser
from galvanalyser.harvester.parsers.parser import Parser
import pandas.errors

class DummyParser(Parser):
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def get_metadata(self):
        return ({'num_rows': 1}, {"dummy column":{}})

    def get_data_generator_for_columns(self, columns=[], first_data_row=0, col_mapping={}):
        return [{'dummy column':0}]


# When saving a data file, call this to parse the data.
def parse_data_file(instance, use_parser):
    if not instance:
        return
    if hasattr(instance, '_dirty'):
        print("moo")
        return

    try:
        # print("result_post_save: Sender: %s, Instance: %s, args: %s, kwargs: %s, base_loc: %s, Filename: %s" % (
        #     sender, instance, args, kwargs, instance.raw_data_file.file.storage.base_location, instance.raw_data_file.file.name))
        filepath = "/".join([instance.raw_data_file.file.storage.base_location, instance.raw_data_file.file.name])
        # TODO: Work out which type of file it is and call the correct parser!
        # parser = BiologicCSVnTSVParser(filepath)
        parser = DummyParser(filepath)
        if use_parser == "biologic":
            parser = BiologicCSVnTSVParser(filepath)
        if use_parser == "maccor":
            parser = MaccorXLSParser(filepath)
        (instance.metadata, columns) = (parser.get_metadata())
        instance.parsed_metadata['columns'] = columns
        instance.parsed_data = [None] * instance.metadata['num_rows']
        gen = parser.get_data_generator_for_columns(columns, 10)
        print(gen)
        for (idx, row) in enumerate(gen):
            print(row)
            instance.parsed_data[idx] = list(row.values())
    except (pandas.errors.ParserError, ValueError) as e:
        print(e)
        raise ValidationError(message={'raw_data_file': "File parsing failed: " + str(e)})

    # save again after setting metadata but don't get into a recursion loop!
    try:
        instance._dirty = True
        instance.save()
    finally:
        del instance._dirty