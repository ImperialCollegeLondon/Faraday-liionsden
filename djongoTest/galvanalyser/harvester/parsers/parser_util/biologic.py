

"""
Based on the test_resources/parser_data/BioLogic_full.txt file
Maps all possible column namings to their standard names
"""
COLUMN_NAME_MAPPING = {
    "Time": ["time", "Time", "time/s"],
    "mode": ["mode"],
    "ox/red": ["ox/red"],
    "error": ["error"],
    "control changes": ["control changes"],
    "Ns changes": ["Ns changes"],
    "counter inc": ["counter inc."],
    "Ns": ["Ns"],
    "I Range": ["I Range"],
    "control/V/mA": ["control/V/mA"],
    "Ecell/V": ["Ecell/V"],
    "I/mA": ["I/mA"],
    "dq/mA_h": ["dq/mA.h"],
    "(Q-Qo)/mA_h": ["(Q-Qo)/mA.h"],
    "Energy/W_h": ["Energy/W.h"],
    "Analog IN 1/V": ["Analog IN 1/V"],  # TODO: Does 1/V change in this context?
    "Analog OUT/V": ["Analog OUT/V"],
    "Energy charge/W_h": ["Energy charge/W.h"],
    "Energy discharge/W_h": ["Energy discharge/W.h"],
    "Capacitance charge/�F": ["Capacitance charge/�F"],
    "Capacitance discharge/�F": ["Capacitance discharge/�F"],
    "x": ["x"],                          # TODO: Is this right? What does it mean and can it change?
    "Q discharge/mA_h": ["Q discharge/mA.h"],
    "Q charge/mA_h": ["Q charge/mA.h"],
    "Capacity/mA_h": ["Capacity/mA.h"],
    "Efficiency/%": ["Efficiency/%"],
    "control/V": ["control/V"],
    "control/mA": ["control/mA"],
    "cycle number": ["cycle number"],
    "P/W": ["P/W"],
    "R/Ohm": ["R/Ohm"],
    "Rec#": ["Rec#", "RecNo"]
}
