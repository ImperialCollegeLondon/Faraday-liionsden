"""
TODO: Mappings can all be defined here! No need for separate files.
"""

GENERIC_COLUMN_MAPPING = {
    "time": "time/s",
    "Time": "time/s",
    "counter inc.": "counter inc",
    "dq/mA.h": "dq/mA_h",
    "(Q-Qo)/mA_h": "(Q-Qo)/mA.h",
    "Energy/W_h": "Energy/W.h",
    "Energy charge/W_h": "Energy charge/W.h",
    "Energy discharge/W_h": "Energy discharge/W.h",
    "Q discharge/mA_h": "Q discharge/mA.h",
    "Q charge/mA_h": "Q charge/mA.h",
    "Capacity/mA_h": "Capacity/mA.h",
    "RecNo": "Rec#",
}

BIOLOGIC_COLUMN_MAPPING = {
    **GENERIC_COLUMN_MAPPING,
    **{"Ewe/V": "Ecell/V"},
}

MACCOR_COLUMN_MAPPING = {
    **GENERIC_COLUMN_MAPPING,
    **{
        "TestTime(s)": "TestTime",
        "StepTime(s)": "StepTime",
    },
}
