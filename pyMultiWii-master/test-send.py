#!/usr/bin/env python

"""test-send.py: Test script to send RC commands to a MultiWii Board."""

__author__ = "Aldo Vargas"
__copyright__ = "Copyright 2014 Aldux.net"

__license__ = "GPL"
__version__ = "1"
__maintainer__ = "Aldo Vargas"
__email__ = "alduxvm@gmail.com"
__status__ = "Development"

from pyMultiwii import MultiWii

if __name__ == "__main__":

    board = MultiWii("/dev/ttyUSB0")
    #board = MultiWii("/dev/tty.usbserial-A801WZA1")

    try:
        while True:
        	#example of 8 RC channels to be send
            data = [1000,1000,1000,1000,1000,1040,1000,1000]
            
            # Old function 
            #board.sendCMD(16,MultiWii.SET_RAW_RC,data)

            #New function that will receive attitude after setting the rc commands
            board.sendCMD(16,MultiWii.SET_RAW_RC,data)
            board.getData(MultiWii.RC)
            
            print(board.rcChannels)
    except Exception as error:
        print("Error on Main: "+str(error))