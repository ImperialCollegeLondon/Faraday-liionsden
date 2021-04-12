import os

import numpy as np
import pandas as pd
import preparenovonix.novonix_io as nio
import preparenovonix.novonix_prep as prep

df_cols = [
    "Time (s)",
    "Step_id",
    "Variable_x",
    "Variable_x_units",
    "Loop_counter",
    "Protocol_line",
    "State",
]

novonix2ignore = ["Date and Time", "Cycle Number", "Circuit Temperature"]
novonix_int = [
    "Step Number",
    "State (0=Start 1=Regular 2=End -1=Single Measurement)",
    "Protocol Line (it refers to the reduced protocol)",
    "Loop number",
]
istep = 0
istate = 1
iprotocol = 2
iloop = 3


def colname_nobrackets(colname):
    """
    Given the name of a column from a novonix file,
    return it without possible units or descriptors
    within brackets

    Parameters
    ----------
    colname : string
        Name of the column

    Returns
    -------
    col_nobrak : string
        Output name

    Examples
    --------
    >>> colname_nobrackets('Capacity (Ah)')
    Capacity
    """

    if "(" in colname:
        cc = colname.split("(")[0]
        col_nobrak = cc.strip()
    else:
        col_nobrak = colname

    return col_nobrak


def get_units(colname):
    """
    Given the name of a column from a novonix file,
    return the units

    Parameters
    ----------
    colname : string
        Name of the column

    Returns
    -------
    units : string
        Units of the columg

    Examples
    --------
    >>> colname_nobrackets('Capacity (Ah)')
    Ah
    """

    units = ""

    if "(" in colname:
        u1 = colname.split("(")[1]
        u2 = u1.split(")")[0]
        units = u2.strip()

    return units


def novonix_importer(file_to_open):
    """
    Given a novonix file name, return a pandas data frame
    to be uploaded to the database

    Parameters
    ----------
    file_to_open : string
        Name of the input file

    Returns
    -------
    full_stacked : pandas data frame


    Examples
    --------
    >>> data2import = novonix_importer('../example_data/novonix_example_data.csv')
    """

    # Prepare the Novonix file
    prep.prepare_novonix(
        file_to_open, addstate=True, lprotocol=True, overwrite=False, verbose=False
    )

    # Get the name of the prepared file
    infile = nio.after_file_name(file_to_open)

    # Find the number of measurements
    nmeasurements = nio.get_num_measurements(infile)

    # Read the columns names
    col_names = nio.get_col_names(infile)

    # Column names without brackets
    # This is done to avoid problems with the degrees symbol
    col_nobrak = [colname_nobrackets(col) for col in col_names]
    novint_nobrak = [colname_nobrackets(col) for col in novonix_int]

    # Create a time array (s)
    col = "Run Time (h)"
    time_m = nio.read_column(infile, col, outtype="float")
    time_m = time_m * 3600.0  # Convert hours into seconds

    # Initialize matrix of integers
    int_m = np.zeros((len(novonix_int), nmeasurements), dtype=np.int)
    int_m.fill(-999)
    for i, col in enumerate(novonix_int):
        int_m[i, :] = nio.read_column(infile, col, outtype="int")

    # Find number of variables and names
    nvars = 0
    for col in col_nobrak:
        if (col in novonix2ignore) or (col in novint_nobrak) or ("time" in col.lower()):
            continue
        else:
            nvars += 1

    # Initialize matrix for variables and units
    var_m = np.zeros((nvars, nmeasurements))
    var_m.fill(-999.0)
    unit_m = np.empty((nvars, nmeasurements), dtype="U10")
    unit_m.fill("-")

    # Populate the variables and units matrices
    ivar = 0
    for ic, col in enumerate(col_nobrak):
        if (col in novonix2ignore) or (col in novint_nobrak) or ("time" in col.lower()):
            continue
        else:
            colname = col_names[ic]
            var_m[ivar, :] = nio.read_column(infile, colname, outtype="float")
            # Get units
            units = get_units(colname)
            unit_m[ivar, :] = units

            ivar += 1

    # Remove the prepared file
    os.remove(infile)

    # Global matrix
    data = []
    for im in range(nmeasurements):
        for iv in range(nvars):
            row = [
                str(time_m[im]),
                str(int_m[istep, im]),
                str(var_m[iv, im]),
                str(unit_m[iv, im]),
                str(int_m[iloop, im]),
                str(int_m[iprotocol, im]),
                str(int_m[istate, im]),
            ]
            data.append(row)

    # Transform matrix into pandas data frame
    full_stacked = pd.DataFrame(columns=df_cols, data=data)

    return full_stacked


if __name__ == "__main__":
    novonix_importer("../example_data/novonix_raw_example_data.csv")
