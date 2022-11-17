import re
from logging import getLogger
from typing import Any, Dict, List, TextIO, Tuple, Union

import pandas as pd
import yaml
from yaml.scanner import ScannerError

from .battery_exceptions import UnsupportedFileTypeError
from .mappings import COLUMN_NAME_MAPPING
from .parsing_engines_base import ParsingEngineBase


class BiologicParsingEngine(ParsingEngineBase):
    """ParserBase for the csv and tsv output of the BioLogic cycler."""

    name = "Biologic"
    description = "Biologic CSV/TSV/MPT"
    valid: List[Tuple[str, str]] = [
        ("text/plain", ".csv"),
        ("text/plain", ".mpt"),
        ("text/plain", ".tsv"),
        ("text/plain", ".txt"),
        ("text/plain", ".mps"),
    ]
    mandatory_columns: Dict[str, Dict[str, Union[str, Tuple[str, str]]]] = {
        "time/s": dict(symbol="t", unit=("Time", "s")),
        "Ecell/V": dict(symbol="V", unit=("Voltage", "V")),
        "I/mA": dict(symbol="I", unit=("Current", "mA")),
        "(Q-Qo)/mA.h": dict(symbol="Q-Q_0", unit=("Charge", "mA·h")),
        "Temperature/ｰC": dict(symbol="T", unit=("Temperature", "C")),
        "Q discharge/mA.h": dict(symbol="Q discharge", unit=("Charge", "mA·h")),
        "Ns changes": dict(symbol="Ns changes", unit=("Unitless", "1")),
        "cycle number": dict(symbol="Cyl", unit=("Unitless", "1")),
    }
    column_name_mapping = COLUMN_NAME_MAPPING

    # Assumed to be this encoding, but it might be different...
    encoding = "iso-8859-1"

    @classmethod
    def factory(cls, file_obj: TextIO) -> ParsingEngineBase:
        """Factory method for creating a parsing engine.

        Args:
            file_obj (TextIO): File to parse.
        """
        skip_rows, file_type = get_header_size(file_obj, cls.encoding)
        # check validity of file
        if file_type in ("invalid", "settings"):
            data = pd.DataFrame([])
            file_metadata = []
            getLogger().error(
                f"File {file_obj.name} cannot be parsed: File type: {file_type}."
            )
        else:
            data = load_biologic_data(file_obj, skip_rows, cls.encoding)
            file_metadata = get_file_header(file_obj, skip_rows, cls.encoding)
        return cls(file_obj, skip_rows, data, file_metadata)


def get_file_header(
    file_obj: TextIO, skip_rows: int, encoding: str
) -> Union[Dict[str, Any], List[Any]]:
    """Extracts the header from the Biologic file.

    Args:
        file_obj (TextIO): File to load the data from.
        skip_rows (int): Location of the header, assumed equal to the number of rows to
            skip.
        encoding (str): Encoding of the file.

    Returns:
        A list of rows for the header, without the termination characters and
        empty lines.
    """
    if skip_rows == 0:
        return []
    with file_obj.open("r") as f:
        header = list(filter(len, (f.readline().rstrip() for _ in range(skip_rows))))
        if type(header[0]) == bytes:
            header = [i.decode(encoding) for i in header]
    try:
        header = header_to_yaml(header)
    except ScannerError:
        getLogger().warning(
            f"File header for {file_obj.name} could not be parsed as YAML format!"
        )
    return header


def get_header_size(file_obj: TextIO, encoding: str) -> Tuple[int, str]:
    """Reads the file and determines the size of the header.

    Args:
        file_obj (TextIO): File to load the data from.
        encoding (str): Encoding of the file.

    Returns:
        Tuple (int, str): The number of rows in the header and a string describing the
            file format. The str can be "valid", "settings" or "invalid" depending on
            whether the file is a valid data file, a settings file, or an invalid file.
    """
    file_obj.seek(0)
    with file_obj.open("r") as f:
        lines = iter([i.decode(encoding) for i in f.readlines()])
        first_line = next(lines)
        # Check if the file starts with a line containing the string "ASCII FILE"
        if "ASCII FILE" in first_line:
            # Read the next line containing header size, returning it as an int
            file_obj.seek(0)
            return (int(re.findall(r"[0-9]+", next(lines))[0]) - 1, "valid")
        elif "SETTING FILE" in first_line:
            file_obj.seek(0)
            return (0, "settings")
        # If the file does not start with "ASCII FILE", check if there is no header
        # and the data starts there
        elif "time/s" in first_line:
            file_obj.seek(0)
            return (0, "valid")
        else:
            file_obj.seek(0)
            return (0, "invalid")


def load_biologic_data(file_obj: TextIO, skip_rows: int, encoding: str) -> pd.DataFrame:
    """Loads the data as a Pandas data frame.

    Can work with files that have a header or that do not have one. It is assumed
    that the separator is a comma (,). If there is only 1 column, it is reloaded
    using tabs. If there is still only 1 column, an erro is raised.

    Args:
        file_obj (TextIO): File to load the data from.
        skip_rows (int): Location of the header, assumed equal to the number of rows to
            skip.
        encoding (str): Encoding of the file.

    Raises:
        UnsupportedFileTypeError: If only one column is found after trying comma and
        tabs as separators.

    Returns:
        pd.DataFrame: A pandas dataframe with all the data.
    """
    kwargs = dict(skiprows=skip_rows, encoding=encoding, encoding_errors="replace")
    file_obj.open("r")
    try:
        file_obj.seek(0)
        data = pd.read_csv(file_obj, delimiter=",", **kwargs)
    except pd.errors.ParserError:
        try:
            file_obj.seek(0)
            data = pd.read_csv(file_obj, delimiter="\t", **kwargs)
        except pd.errors.ParserError as err:
            raise UnsupportedFileTypeError(err)

    if len(data.columns) == 1:
        file_obj.seek(0)
        data = pd.read_csv(file_obj, delimiter="\t", **kwargs)

    if len(data.columns) == 1:
        raise UnsupportedFileTypeError()

    return data


yaml_replacements = {
    "\t": "    ",  # tabs form lists. in YAML, tab indents are not valid
    "Modulo Bat": "Mode: Modulo Bat",
    "for windows": "for windows : ",
    "Internet server": "Internet server : ",
    "Command interpretor": "Command interpretor : ",
    "for DX =": "DX/DQ : for DX =",
    "Record": "Record : ",
    "CE vs. WE compliance": "CE vs. WE compliance :",
}


def header_to_yaml(header: List[str]) -> Dict:
    """Adapt BioLog file header to YAML format.

    The format of the BioLogix header is "almost" parsable directly as YAML We can hack
    in a few string replacements to make it valid. Table containg per-column metadata
    is not parseable as YAML. We skip this for now - find line where it starts,
    and end there.

    TODO: The table-like part of the header contains useful information related to the
    cycler protocol. This should be extracted somehow and making it available.

    Args:
        header: The header as a list fo strings.

    Returns:
        A dictionary parsed by YAML
    """

    # 1) Apply replacements
    regex = re.compile("(%s)" % "|".join(map(re.escape, yaml_replacements.keys())))
    rep_header = [
        regex.sub(lambda mo: yaml_replacements.get(mo.group(), f"{h}"), h)
        for h in header
    ]

    # 2) Find parseable data before the table-like region
    parseable_lines = []
    for line in rep_header:
        if line.startswith("Ns"):
            break

        if "ASCII FILE" in line:
            line = "FileType : " + line

        parseable_lines.append(line)

    # 3) Parse the header using YAML
    return yaml.safe_load("\n".join(parseable_lines))
