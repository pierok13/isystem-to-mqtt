""" Definition of Modbus adress and convertions to apply """

from .tag_definition import TagDefinition, WriteTagDefinition, MultipleTagDefinition
from . import convert


def get_tables(model):
    """ Return the address definition depending of model. """
    if model == "modulens-o":
        return (READ_TABLE_MODULENS_O, WRITE_TABLE_MODULENS_O, ZONE_TABLE_MODULENS_O)
    if model == "diematic3":
        return (READ_TABLE_DIEMATIC3, WRITE_TABLE_DIEMATIC3, ZONE_TABLE_DIEMATIC3)
    return (None, None, None)
ZONE_TABLE_DIEMATIC3 = [
                         (3, 4),
                         (108, 3),
                         (7, 3),
                         (13, 3),
                         (14, 8),
                         (0,  0),
                         (23, 11),
                         (38, 1),
                         (59, 4),
                         (68, 4),
                         (0,  0),
                         (74, 5),
                         (89, 7),
                         (96, 1),
                         (453, 1),
                         (456, 1),
                         (465, 1),
                         (0,  0),
                         (126, 21),
                         (147, 21),
                         (189, 21),
#                        (231, 2),
                        ]

READ_TABLE_DIEMATIC3 = {
    3: TagDefinition("system/ctrl", convert.unit),
    4: TagDefinition("system/hour", convert.unit),
    5: TagDefinition("system/minute", convert.unit),
    6: TagDefinition("system/day-of-week", convert.unit),
    108: TagDefinition("system/day", convert.unit),
    109: TagDefinition("system/month", convert.unit),
    110: TagDefinition("system/year", convert.unit),
    7: TagDefinition("outside/temperature", convert.tenth),
    8: TagDefinition("boiler/summer-setpoint", convert.tenth),
    9: TagDefinition("outside/antifreeze-temperature", convert.tenth),
    13: TagDefinition("system/HollydaysPeriod", convert.tenth),

    14: TagDefinition("zone-a/day-target-temperature", convert.tenth),
    15: TagDefinition("zone-a/night-target-temperature", convert.tenth),
    16: TagDefinition("zone-a/antifreeze-target-temperature", convert.tenth),
    17: MultipleTagDefinition([("zone-a/mode", convert.derog_bit),
                                ("zone-a/mode-raw", convert.unit),
                                ("zone-a/mode-simple", convert.derog_bit_simple)]),
    18: TagDefinition("zone-a/sensor-temperature", convert.tenth),
    19: TagDefinition("zone-a/sensor-influence", convert.unit),
    20: TagDefinition("zone-a/slope-heating-curvey", convert.tenth),
    21: TagDefinition("zone-a/calculated-temperature", convert.tenth),

    23: TagDefinition("zone-b/day-target-temperature", convert.tenth),
    24: TagDefinition("zone-b/night-target-temperature", convert.tenth),
    25: TagDefinition("zone-b/antifreeze-target-temperature", convert.tenth),
    26: MultipleTagDefinition([("zone-b/mode", convert.derog_bit),
                                ("zone-b/mode-raw", convert.unit),
                                ("zone-b/mode-raw-simple", convert.derog_bit_simple),
                                ("zone-b/mode-simple", convert.derog_bit_simple)
                              ]),
    27: TagDefinition("zone-b/sensor-temperature", convert.tenth),
    28: TagDefinition("zone-b/sensor-influence", convert.unit),
    29: TagDefinition("zone-b/slope-heating-curvey", convert.tenth),
    30: TagDefinition("zone-b/departure-temperature-min", convert.tenth),
    31: TagDefinition("zone-b/departure-temperature-max", convert.tenth),
    32: TagDefinition("zone-b/calculated-temperature", convert.tenth),
    33: TagDefinition("zone-b/departure-temperature", convert.tenth),

    38: MultipleTagDefinition([("dhw/mode", convert.derog_bit),
                                ("dhw/mode-raw", convert.unit),
                                ("dhw/mode-simple", convert.derog_bit_simple)
                              ]),

    59: TagDefinition("dhw/day-target-temperature", convert.tenth),
    60: TagDefinition("dhw/priority", convert.unit),
    61: TagDefinition("dhw/pump-delay", convert.unit),
    62: TagDefinition("dhw/temperature", convert.tenth),
    96: TagDefinition("dhw/night-target-temperature", convert.tenth),
    68: TagDefinition("boiler/day-curve-footprint", convert.tenth),
    69: TagDefinition("boiler/night-curve-footprint", convert.tenth),

    70: TagDefinition("boiler/min-temperature", convert.tenth),
    71: TagDefinition("boiler/max-temperature", convert.tenth),

    74: TagDefinition("boiler/calculated-temperature", convert.tenth),
    75: TagDefinition("boiler/temperature", convert.tenth),
    76: TagDefinition("boiler/smoke-temperature", convert.tenth),
    77: TagDefinition("boiler/burner/starts", convert.bcd_ten),
    78: TagDefinition("boiler/burner/hours", convert.bcd_ten),

    89: MultipleTagDefinition([ ("boiler/base-and-ecs", convert.unit),
                                ("boiler/pump-aux", convert.readbit0),
                                ("boiler/burner-status", convert.readbit3),
                                ("zone-a/pump", convert.readbit4),
                                ("dhw/pump", convert.readbit5),
                                ]),
    90: MultipleTagDefinition([ ("boiler/options-b-and-c", convert.unit),
                                ("zone-b/valve/closing", convert.readbit0),
                                ("zone-b/valve/opening", convert.readbit1),
                                ("zone-b/pump", convert.readbit4),
                                ]),
    91: TagDefinition("boiler/terminal2", convert.unit),
    92: TagDefinition("boiler/terminal3", convert.unit),
    93: TagDefinition("boiler/option-c", convert.unit),
    94: TagDefinition("boiler/telecommand1", convert.unit),
    95: TagDefinition("boiler/telecommand2", convert.unit),
    126: TagDefinition("zone-a/schedule", convert.json_week_schedule, 21),
    147: TagDefinition("zone-b/schedule", convert.json_week_schedule, 21),
    189: TagDefinition("dhw/schedule", convert.json_week_schedule, 21),

    453: TagDefinition("boiler/return-temperature", convert.tenth),
    456: TagDefinition("boiler/pressure", convert.tenth),

    231: TagDefinition("zone-a/program", convert.unit),
    232: TagDefinition("zone-b/program", convert.unit),

    465: TagDefinition("boiler/failure", convert.unit),
}

WRITE_TABLE_DIEMATIC3 = {
    "system/hour/SET": WriteTagDefinition(4, convert.write_unit),
    "system/minute/SET": WriteTagDefinition(5, convert.write_unit),
    "system/day-of-week/SET": WriteTagDefinition(6, convert.write_unit),
    "system/day/SET": WriteTagDefinition(108, convert.write_unit),
    "system/month/SET": WriteTagDefinition(109, convert.write_unit),
    "system/year/SET": WriteTagDefinition(110, convert.write_unit),

    "zone-a/mode-simple/SET": WriteTagDefinition(17, convert.write_derog_bit_simple),
    "zone-a/mode-raw/SET": WriteTagDefinition(17, convert.write_unit),
    "zone-a/day-target-temperature/SET": WriteTagDefinition(14, convert.write_tenth),
    "zone-a/night-target-temperature/SET": WriteTagDefinition(15, convert.write_tenth),

    "zone-b/mode-simple/SET": WriteTagDefinition(26, convert.write_derog_bit_simple),
    "zone-b/mode-raw/SET": WriteTagDefinition(26, convert.write_unit),
    "zone-b/day-target-temperature/SET": WriteTagDefinition(23, convert.write_tenth),
    "zone-b/night-target-temperature/SET": WriteTagDefinition(24, convert.write_tenth),

    "dhw/day-target-temperature/SET": WriteTagDefinition(59, convert.write_tenth),
    "dhw/night-target-temperature/SET": WriteTagDefinition(96, convert.write_tenth),
    "dhw/mode-raw/SET": WriteTagDefinition(38, convert.write_unit),
    "dhw/mode-simple/SET" : WriteTagDefinition(38, convert.write_derog_bit_simple),

    "zone-a/program/SET": WriteTagDefinition(231, convert.write_unit),
    "zone-b/program/SET": WriteTagDefinition(232, convert.write_unit),

}


ZONE_TABLE_MODULENS_O = [(231, 20),
                         (507, 4),
                         (471, 10),
                         (600, 21),
                         (637, 24),
                         (721, 4),
                         (788, 9),]

READ_TABLE_MODULENS_O = {
    3: TagDefinition("boiler/version", convert.unit),
    4: TagDefinition("boiler/time", convert.hours_minutes_secondes, 3),
    7: TagDefinition("outside/temperature", convert.tenth),
    8: TagDefinition("boiler/summer-setpoint", convert.tenth),
    9: TagDefinition("outside/antifreeze", convert.tenth),
    10: TagDefinition("boiler/decrease-mode", convert.decrease),
    11: TagDefinition("boiler/pump-postrun", convert.unit),
    12: TagDefinition("boiler/auto-adaptative", convert.off_on), #FIXME inverse sur ma chaudiere
    14: TagDefinition("zone-a/day-target-temperature", convert.tenth),
    15: TagDefinition("zone-a/night-target-temperature", convert.tenth),
    16: TagDefinition("zone-a/antifreeze-target-temperature", convert.tenth),
    17: MultipleTagDefinition([("zone-a/mode", convert.derog_bit),
                               ("zone-a/mode-raw", convert.unit),
                               ("zone-a/mode-simple", convert.derog_bit_simple)]),
    18: TagDefinition("zone-a/temperature", convert.tenth),
    19: TagDefinition("zone-a/sensor-influence", convert.unit),
    20: TagDefinition("zone-a/curve", convert.tenth),
    21: TagDefinition("zone-a/calculated-temperature", convert.tenth),
    23: TagDefinition("zone-b/day-target-temperature", convert.tenth),
    24: TagDefinition("zone-b/night-target-temperature", convert.tenth),
    25: TagDefinition("zone-b/antifreeze-target-temperature", convert.tenth),
    26: MultipleTagDefinition([("zone-b/mode", convert.derog_bit),
                               ("zone-b/mode-raw", convert.unit),
                               ("zone-b/mode-simple", convert.derog_bit_simple)]),
    27: TagDefinition("zone-b/temperature", convert.tenth),
    28: TagDefinition("zone-b/sensor-influence", convert.unit),
    29: TagDefinition("zone-b/curve", convert.tenth),
    30: TagDefinition("zone-b/water-min-temperature", convert.tenth),
    31: TagDefinition("zone-b/water-max-temperature", convert.tenth),
    32: TagDefinition("zone-b/calculated-temperature", convert.tenth),
    33: TagDefinition("zone-b/water-temperature", convert.tenth),
    35: TagDefinition("zone-c/day-target-temperature", convert.tenth),
    36: TagDefinition("zone-c/night-target-temperature", convert.tenth),
    37: TagDefinition("zone-c/antifreeze-target-temperature", convert.tenth),
    38: MultipleTagDefinition([("zone-c/mode", convert.derog_bit),
                               ("zone-c/mode-raw", convert.unit),
                               ("zone-c/mode-simple", convert.derog_bit_simple)]),
    39: TagDefinition("zone-c/temperature", convert.tenth),
    40: TagDefinition("zone-c/sensor-influence", convert.unit),
    41: TagDefinition("zone-c/curve", convert.tenth),
    42: TagDefinition("zone-c/water-min-temperature", convert.tenth),
    43: TagDefinition("zone-c/water-max-temperature", convert.tenth),
    44: TagDefinition("zone-c/calculated-temperature", convert.tenth),
    45: TagDefinition("zone-c/water-temperature", convert.tenth),
    59: TagDefinition("dhw/target-temperature", convert.tenth),
    60: TagDefinition("dhw/priority", convert.unit), #TODO add specific convert
    61: TagDefinition("dhw/pump-postrun", convert.unit),
    62: TagDefinition("dhw/temperature", convert.tenth),
    64: TagDefinition("boiler/leading-boiler", convert.unit),
    68: TagDefinition("boiler/day-curve-footprint", convert.tenth),
    69: TagDefinition("boiler/night-curve-footprint", convert.tenth),
    70: TagDefinition("boiler/min-temperature", convert.tenth),
    71: TagDefinition("boiler/max-temperature", convert.tenth),
    72: TagDefinition("boiler/diff-a", convert.tenth),
    73: TagDefinition("boiler/diff-b", convert.tenth),
    74: TagDefinition("boiler/calculated-temperature", convert.tenth),
    75: TagDefinition("boiler/temperature", convert.tenth),
    76: TagDefinition("boiler/smoke-temp", convert.unit),
    77: TagDefinition("boiler/start-count-tenth", convert.unit),
    78: TagDefinition("boiler/hours-count-tenth", convert.unit),
    89: TagDefinition("boiler/base-ecs", convert.base_ecs),
    96: TagDefinition("dhw/night-target-temperature", convert.tenth),
    102: TagDefinition("outside/mean-temperature", convert.tenth),
    108: TagDefinition("boiler/date", convert.day_mounth_year, 3),
    117: TagDefinition("boiler/temperature", convert.tenth),
    121: TagDefinition("dhw/target-temperature", convert.tenth),
    126: TagDefinition("zone-a/schedule", convert.json_week_schedule, 21),
    147: TagDefinition("zone-b/schedule", convert.json_week_schedule, 21),
    168: TagDefinition("zone-c/schedule", convert.json_week_schedule, 21),
    189: TagDefinition("dhw/schedule", convert.json_week_schedule, 21),
    231: TagDefinition("zone-a/program", convert.unit),
    232: TagDefinition("zone-b/program", convert.unit),
    233: TagDefinition("zone-c/program", convert.unit),
    247: TagDefinition("zone-a/autoadapt-shift", convert.tenth),
    248: TagDefinition("zone-b/autoadapt-shift", convert.tenth),
    249: TagDefinition("zone-c/autoadapt-shift", convert.tenth),
    251: TagDefinition("boiler/start-count-unit", convert.unit),
    252: TagDefinition("boiler/hours-count-unit", convert.unit),
    264: TagDefinition("boiler/building-inertia", convert.unit),
    266: TagDefinition("boiler/bandwidth", convert.tenth),
    267: TagDefinition("boiler/3WV-shift", convert.tenth),
    269: TagDefinition("boiler/minimum-runing-time", convert.unit),
    271: TagDefinition("boiler/burner-temporisation", convert.unit),
    272: TagDefinition("boiler/pump-postrun", convert.unit),
    274: TagDefinition("outside/calibration", convert.tenth),
    275: TagDefinition("zone-a/calibration", convert.tenth),
    276: TagDefinition("zone-b/calibration", convert.tenth),
    277: TagDefinition("zone-c/calibration", convert.tenth),
    282: TagDefinition("zone-a/anticipation", convert.anticipation),
    283: TagDefinition("zone-b/anticipation", convert.anticipation),
    284: TagDefinition("zone-c/anticipation", convert.anticipation),
    289: TagDefinition("zone-a/day-curve-footprint", convert.footprint),
    290: TagDefinition("zone-a/night-curve-footprint", convert.footprint),
    291: TagDefinition("zone-b/day-curve-footprint", convert.footprint),
    292: TagDefinition("zone-b/night-curve-footprint", convert.footprint),
    298: TagDefinition("zone-a/water-min-temperature", convert.tenth),
    299: TagDefinition("zone-a/water-max-temperature", convert.tenth),
    358: TagDefinition("zone-c/day-curve-footprint", convert.tenth),
    359: TagDefinition("zone-c/night-curve-footprint", convert.tenth),
    437: TagDefinition("boiler/pressure", convert.tenth),
    452: TagDefinition("boiler/temperature", convert.tenth),
    453: TagDefinition("boiler/return-temperature", convert.tenth),
    454: TagDefinition("boiler/smoke-temperature", convert.tenth),
    455: MultipleTagDefinition([("boiler/fan-speed", convert.fan),
                                ("boiler/fan-raw", convert.unit)]),
    459: TagDefinition("dhw/temperature", convert.tenth),
    462: TagDefinition("boiler/calculated-temperature", convert.tenth),
    471: TagDefinition("boiler/power-inst", convert.tenth),
    472: TagDefinition("boiler/power-average", convert.tenth),
    473: TagDefinition("boiler/modulated-power", convert.unit),
    474: TagDefinition("boiler/output-state", convert.output_state, 2),
    507: TagDefinition("boiler/start-count", convert.unit_and_ten, 2),
    509: TagDefinition("boiler/hours-count", convert.unit_and_ten, 2),
    601: TagDefinition("outside/temperature", convert.tenth),
    602: TagDefinition("boiler/temperature", convert.tenth),
    603: TagDefinition("dhw/temperature", convert.tenth),
    604: TagDefinition("boiler/smoke-temperature", convert.tenth),
    605: TagDefinition("zone-b/water-temperature", convert.tenth),
    606: TagDefinition("zone-c/water-temperature", convert.tenth),
    607: TagDefinition("boiler/return-temperature", convert.tenth),
    608: TagDefinition("boiler/ionization-current", convert.tenth),
    609: MultipleTagDefinition([("boiler/fan-speed", convert.fan),
                                ("boiler/fan-raw", convert.unit)]),
    610: TagDefinition("boiler/pressure", convert.tenth),
    614: TagDefinition("zone-a/temperature", convert.tenth),
    615: TagDefinition("zone-a/calculated-temperature", convert.tenth),
    616: TagDefinition("zone-b/temperature", convert.tenth),
    617: TagDefinition("zone-b/calculated-temperature", convert.tenth),
    618: TagDefinition("zone-c/temperature", convert.tenth),
    619: TagDefinition("zone-c/calculated-temperature", convert.tenth),
    620: TagDefinition("boiler/calculated-temperature", convert.tenth),
    622: TagDefinition("boiler/aux1-temperature", convert.tenth),
    623: TagDefinition("boiler/aux2-temperature", convert.tenth),
    624: TagDefinition("boiler/e-univ-temperature", convert.tenth),
    625: TagDefinition("boiler/exchange-temperature", convert.tenth),
    637: TagDefinition("zone-a/active-mode", convert.active_mode),
    638: TagDefinition("zone-b/active-mode", convert.active_mode),
    639: TagDefinition("zone-c/active-mode", convert.active_mode),
    640: TagDefinition("dhw/active-mode", convert.active_mode),
    641: TagDefinition("zone-aux/active-mode", convert.active_mode),
    644: TagDefinition("boiler/active-mode", convert.boiler_mode),
    650: TagDefinition("zone-a/day-target-temperature", convert.tenth),
    651: TagDefinition("zone-a/night-target-temperature", convert.tenth),
    652: TagDefinition("zone-a/antifreeze-target-temperature", convert.tenth),
    653: MultipleTagDefinition([("zone-a/mode", convert.derog_bit),
                                ("zone-a/mode-raw", convert.unit),
                                ("zone-a/mode-simple", convert.derog_bit_simple)]),
    654: TagDefinition("zone-a/sensor-influence", convert.unit),
    655: TagDefinition("zone-a/curve", convert.tenth),
    656: TagDefinition("zone-b/day-target-temperature", convert.tenth),
    657: TagDefinition("zone-b/night-target-temperature", convert.tenth),
    658: TagDefinition("zone-b/antifreeze-target-temperature", convert.tenth),
    659: MultipleTagDefinition([("zone-b/mode", convert.derog_bit),
                                ("zone-b/mode-raw", convert.unit),
                                ("zone-b/mode-simple", convert.derog_bit_simple)]),
    660: TagDefinition("zone-b/sensor-influence", convert.unit),
    661: TagDefinition("zone-b/curve", convert.tenth),
    662: TagDefinition("zone-b/water-min-temperature", convert.tenth),
    663: TagDefinition("zone-b/water-max-temperature", convert.tenth),
    664: TagDefinition("zone-c/day-target-temperature", convert.tenth),
    665: TagDefinition("zone-c/night-target-temperature", convert.tenth),
    666: TagDefinition("zone-c/antifreeze-target-temperature", convert.tenth),
    667: MultipleTagDefinition([("zone-c/mode", convert.derog_bit),
                                ("zone-c/mode-raw", convert.unit),
                                ("zone-c/mode-simple", convert.derog_bit_simple)]),
    668: TagDefinition("zone-c/sensor-influence", convert.unit),
    669: TagDefinition("zone-c/curve", convert.tenth),
    670: TagDefinition("zone-c/water-min-temperature", convert.tenth),
    671: TagDefinition("zone-c/water-max-temperature", convert.tenth),
    672: TagDefinition("dhw/day-target-temperature", convert.tenth),
    673: TagDefinition("dhw/night-target-temperature", convert.tenth),
    677: TagDefinition("boiler/min-temperature", convert.tenth),
    678: TagDefinition("boiler/max-temperature", convert.tenth),
    679: TagDefinition("boiler/hours-minute", convert.hours_minutes, 2),
    681: TagDefinition("boiler/date", convert.day_mounth_year, 3),
    710: TagDefinition("boiler/pcu-stat", convert.unit),
    711: TagDefinition("boiler/pcu-substat", convert.unit),
    712: TagDefinition("boiler/pcu-block", convert.unit),
    713: TagDefinition("boiler/pcu-lock", convert.unit),
    721: TagDefinition("zone-a/antifreeze-duration", convert.unit),
    724: TagDefinition("zone-b/antifreeze-duration", convert.unit),
    727: TagDefinition("zone-c/antifreeze-duration", convert.unit),
    734: TagDefinition("boiler/second-calculated-temperature", convert.tenth),
    735: TagDefinition("boiler/state", convert.unit),
    770: TagDefinition("boiler/hours-minute", convert.hours_minutes, 2),
    773: TagDefinition("boiler/date", convert.day_mounth_year, 3),
    788: TagDefinition("boiler/heating-power", convert.power, 3),
    791: TagDefinition("boiler/dhw-power", convert.power, 3),
    794: TagDefinition("boiler/cooling-power", convert.power, 3)

}

WRITE_TABLE_MODULENS_O = {
    # "zone-a/antifreeze-duration/SET": WriteTagDefinition(13, convert.write_unit),
    "zone-a/program/SET": WriteTagDefinition(231, convert.write_unit),
    "zone-a/mode-simple/SET": WriteTagDefinition(653, convert.write_derog_bit_simple),
    "zone-a/mode-raw/SET": WriteTagDefinition(653, convert.write_unit),
    # antifreeze-duration do not work, boiler ignore value
    "zone-a/antifreeze-duration/SET": WriteTagDefinition(721, convert.write_unit),
    "zone-a/day-target-temperature/SET": WriteTagDefinition(650, convert.write_tenth),
    "zone-a/night-target-temperature/SET": WriteTagDefinition(651, convert.write_tenth),

    "zone-b/program/SET": WriteTagDefinition(232, convert.write_unit),
    "zone-b/mode-simple/SET": WriteTagDefinition(659, convert.write_derog_bit_simple),
    "zone-b/mode-raw/SET": WriteTagDefinition(659, convert.write_unit),
    "zone-b/antifreeze-duration/SET": WriteTagDefinition(724, convert.write_unit),
    "zone-b/day-target-temperature/SET": WriteTagDefinition(656, convert.write_tenth),
    "zone-b/night-target-temperature/SET": WriteTagDefinition(657, convert.write_tenth),
}
