#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import logging
import time
#import minimalmodbus
import isystem_to_mqtt.isystem_modbus

import isystem_to_mqtt.tables

parser = argparse.ArgumentParser()
parser.add_argument("--start", help="Start adress default=0.", type=int, default=0)
parser.add_argument("--number", help="Number of word to read.", type=int, default=838)
parser.add_argument("--stop_bit", help="stop bit, default 1", type=int, default=1)
parser.add_argument("--parity", help="parity, default N", default="N")
parser.add_argument("--data_bit", help="databits, default 8", type=int, default=8)
parser.add_argument("--baud", help="baudrate, default 9600", type=int, default=9600)
parser.add_argument("--serial", help="Serial interface, default /dev/serial0",
                    default="/dev/serial0")
parser.add_argument("--deviceid", help="Modbus device id, default 10",
                    type=int, default=10)
parser.add_argument("--log", help="Logging level, default INFO",
                    default="INFO")
parser.add_argument("--bimaster", help="bi-master mode (5s for peer, 5s for us)",
                    action="store_true")
parser.add_argument("--model", help="boiler model",
                    default="modulens-o")
args = parser.parse_args()

# Convert to upper case to allow the user to
# specify --log=DEBUG or --log=debug
numeric_level = getattr(logging, args.log.upper(), None)
if not isinstance(numeric_level, int):
    raise ValueError("Invalid log level: {0}".format(args.log))
logging.basicConfig(level=numeric_level)

_LOGGER = logging.getLogger(__name__)


(READ_TABLE, WRITE_TABLE, READ_ZONES) = isystem_to_mqtt.tables.get_tables(args.model)



# Initialisation of Modbus
instrument = isystem_to_mqtt.isystem_modbus.ISystemInstrument(args.serial,
                                                              args.baud,
                                                              args.parity,
                                                              args.data_bit,
                                                              args.stop_bit,
                                                              args.bimaster)
#instrument.debug = False   # True or False


def read_zone(base_address, number_of_value):
    """ Read a MODBUS table zone and dump raw and converted. """
    instrument.connect()
    #Set Slave ID number
    instrument.set_slave(args.deviceid)

    #Enable RPi GPIO Functions
    instrument.enable_rpi(1)

    #Define pin numbers to be used as Read Enable (RE) and Drive Enable (DE)
    instrument.configure_rpi_bcm_pins(isystem_to_mqtt.isystem_modbus.BCM_PIN_DE,isystem_to_mqtt.isystem_modbus.BCM_PIN_RE)

    #Export pin direction (set as outputs)
    instrument.rpi_pin_export_direction()
    
    try:
        raw_values = instrument.read_registers(base_address, number_of_value)
    except EnvironmentError:
        logging.exception("I/O error")
    except ValueError:
        logging.exception("Value error")
    else:
        next_not_used_adress = 0
        for index in range(0, number_of_value):
            address = base_address + index
            print("{0:4d} => {1:5d} ".format(address, raw_values[index]), end='')
            tag_definition = READ_TABLE.get(address)
            if tag_definition:
                tag_definition.print(raw_values, index)
                next_not_used_adress = max(
                    next_not_used_adress,
                    address + tag_definition.needed_value)
            else:
                if address < next_not_used_adress:
                    print("^", end='')
            print("")
        instrument.rpi_pin_unexport_direction()
        instrument.close()
instrument.wait_time_slot()


MAX_NUMBER_BY_READ = 123

# The total read time must be under the time slot duration
start_time = time.time()

for start_address in range(args.start, args.start + args.number, MAX_NUMBER_BY_READ):
    read_zone(start_address, min(MAX_NUMBER_BY_READ, args.start + args.number - start_address))

    duration = time.time() - start_time
    _LOGGER.debug("Read take %1.3fs", duration)
    if duration > isystem_to_mqtt.isystem_modbus.MAXIMUM_OPERATION:
        instrument.wait_time_slot()
        start_time = time.time()


