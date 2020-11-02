from django.core.exceptions import ValidationError
from galvanalyser.harvester.parsers.biologic_parser import BiologicCSVnTSVParser
from galvanalyser.harvester.parsers.maccor_parser import MaccorXLSParser
import pandas.errors

# When saving a data file, call this to parse the data.
def parse_data_file(instance):
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
        parser = MaccorXLSParser(filepath)
        (instance.metadata, columns) = (parser.get_metadata())
        instance.parsed_metadata['columns'] = columns
        instance.parsed_data['rows'] = [None] * instance.metadata['num_rows']
        gen = parser.get_data_generator_for_columns(columns, 10)
        print(gen)
        for (idx, row) in enumerate(gen):
            print(row)
            instance.parsed_data['rows'][idx] = list(row.values())
        instance.parsed_data['columns'] = list(row.keys())
    except (pandas.errors.ParserError, ValueError) as e:
        print(e)
        raise ValidationError(message={'raw_data_file': "File parsing failed: " + str(e)})

    # save again after setting metadata but don't get into a recursion loop!
    try:
        instance._dirty = True
        instance.save()
    finally:
        del instance._dirty