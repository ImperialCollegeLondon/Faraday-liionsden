import abc
from enum import Enum
from typing import List, Dict, Generator, Set

Vector = List[Dict]


class FileType(Enum):
    """Different file types"""
    MACCOR_CSV = 1
    MACCOR_TSV = 2
    MACCOR_XLS = 3
    NOVONIX = 4
    BIOLOGIC = 5
    IVIUM_TXT = 6


class Parser(abc.ABC):

    @abc.abstractmethod
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    @abc.abstractmethod
    def get_metadata(self) -> (Dict, Dict):
        pass

    @abc.abstractmethod
    def get_data_generator_for_columns(self, columns: Set, first_data_row: int, col_mapping: Dict) \
            -> Generator[Dict, None, None]:
        pass
