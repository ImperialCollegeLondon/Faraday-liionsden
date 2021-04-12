import pandas as pd
import numpy as np


def biologic_importer(read_filepath):
    """
    Function that reads text file output from biologic and creates a file that is in
    an acceptable format to be added to the database
    Arguments:
    read_filepath: string that contains the filepath to the raw biologic text file
    """
    # Read the Biologic text file into pandas dataframe
    raw = pd.read_csv(read_filepath, ",", engine="python")
    if len(raw.keys()) == 1:
        raw = pd.read_csv(read_filepath, "\t", engine="python")
    # Sometimes unnamed column crops up, not a variable or any sort of state may end
    # up being more than one
    for col_name in raw.keys():
        # check if column name is unnamed, if not, next
        if "Unnam" not in col_name:
            continue
        # else drop column
        raw.drop(col_name, axis=1, inplace=True)
    # Add record number column to the data
    raw["RecNo"] = range(len(raw))
    mandatory_state_columns = []
    # Convert to time in seconds if user has exported as datetime
    if raw["Time"][0] != "Seconds":
        raw["Time"] = pd.to_datetime(raw["Time"])
        raw["Time"] = (raw["Time"] - raw["Time"][0]) / np.timedelta64(1, "s")
        # These are the columns which we want in every row
        mandatory_state_columns = ["Ns", "Time", "RecNo"]
    # check all mandatory columns in df
    if not set(mandatory_state_columns).issubset(set(raw.keys())):
        raise Exception(
            "Not all mandatory state columns present in the data. Please ensure Ns, "
            "time/s & error are all present"
        )
    # copy mandatory into own df
    state_data = raw.loc[:, mandatory_state_columns].copy()
    # get rid of rest of state data
    unwanted_state_columns = [
        "mode",
        "ox/red",
        "cantrol changes",
        "Ns changes",
        "counter inc.",
        "I Range",
        "control/V/mA",
    ]
    # we dont care about this
    # drop all state data except RecNo
    for column in mandatory_state_columns + unwanted_state_columns:
        if column == "RecNo":
            continue
        # if column not in the data, carry on
        try:
            raw.drop(column, axis=1, inplace=True)
        except KeyError:
            pass
    # melt the data so that variable columns now become one column
    stacked = (
        raw.melt("RecNo", value_name="value")
        .sort_values("RecNo")
        .reset_index(drop=True)
    )
    # find how many variables (how many times more rows are now present)
    number_of_vars = int(len(stacked) / len(raw))
    # repeat the state data rows and sort by record number then drop the record number column
    # ready for appending to stacked data
    state_repeated = (
        pd.concat([state_data] * number_of_vars)
        .sort_index()
        .reset_index(drop=True)
        .drop("RecNo", axis=1)
    )
    # merge state and the variable data
    full_stacked = pd.concat([stacked, state_repeated], axis=1)
    # rename columns to fit into database
    full_stacked.rename(columns={"Ns": "StepNo"}, inplace=True)
    full_stacked.rename(columns={"Time": "time"}, inplace=True)
    return full_stacked
