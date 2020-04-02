""" specialized version of modbus for isystem with
master mode """

import logging
import os
import serial
#from minimalmodbus import Instrument, serial, MODE_RTU
from pylibmodbus import ModbusRtu

_LOGGER = logging.getLogger(__name__)

# Bi master timeslot
# peer is master for 5s then we can be master for 5s
# timeout to 400ms
TIME_SLOT = 5
WAITING_TIMEOUT = 0.4
# Wait a maximum of 3 cycle SLAVE => MASTER => SLAVE
MAXIMUM_LOOP = 1 + int(TIME_SLOT * 3 / WAITING_TIMEOUT)
MAXIMUM_OPERATION = TIME_SLOT - WAITING_TIMEOUT
BCM_PIN_DE=17
BCM_PIN_RE=27

class ISystemInstrument(ModbusRtu):
    """ Modbus instrument dedicated to Isystem """
    def __init__(self, device="/dev/serial0", baud=9600, parity="N", data_bit=8, stop_bit=1, bimaster=True):
        ModbusRtu.__init__(self, device, baud, parity, data_bit, stop_bit)
        self.serial.baudrate = baud
        self.serial.bytesize = data_bit
        self.serial.parity = parity
        self.serial.stopbits = stop_bit
        self.serial.timeout = 1
        self.bimaster = bimaster


    def wait_time_slot(self):
        """ In bi-master mode, wait for the 5s boiler is slave. """
        # if not in bimaster mode no need to wait
        if not self.bimaster:
            return

        self.serial.timeout = WAITING_TIMEOUT
        # read until boiler is master
        self.serial.close()
        self.serial.open()
        data = b''
        number_of_wait = 0
        _LOGGER.debug("Wait the peer to be master.")
        #wait a maximum of 6 seconds
        while len(data) == 0 and number_of_wait < MAXIMUM_LOOP:
            data = self.serial.read(100)
            number_of_wait += 1
        if number_of_wait >= MAXIMUM_LOOP:
            _LOGGER.warning("Never get data from peer. Remove --bimaster flag.")
        # the master is the boiler wait for the end of data
        _LOGGER.debug("Wait the peer to be slave.")
        while len(data) != 0:
            data = self.serial.read(100)
        self.serial.close()
        self.serial.timeout = 1.0
        _LOGGER.debug("We are master.")
        # we are master for a maximum of  4.6s (5s - 400ms)

