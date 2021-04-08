from galvanalyser.harvester.battery_exceptions import UnsupportedFileTypeError
from galvanalyser.harvester.parsers.biologic_parser import BiologicCSVnTSVParser
from galvanalyser.harvester.parsers.maccor_parser import MaccorXLSParser
from galvanalyser.harvester.parsers.parser import FileType, Parser


def get_parser(format: FileType, file_path: str) -> Parser:
    """ This factory creates the correct parser for each type of raw data """
    if format == FileType.MACCOR_XLS:
        return MaccorXLSParser(file_path)
    # if format == FileType.MACCOR_TSV:
    #     return MaccorTSVParser(file_path)
    # if format == FileType.MACCOR_CSV:
    #     return MaccorCSVParser(file_path)
    if format == FileType.BIOLOGIC:
        return BiologicCSVnTSVParser(file_path)
    raise UnsupportedFileTypeError("Parser for this filetype is not yet implemented!")
