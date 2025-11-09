'''
Poll arduino info only when requested (for example, we are not updating the pygame interface on a thread; we are just updating it every loop. Why dont we try just querying when we update the interface?)
Usage:

a = ArdyCommy() #Initialize an ArdyCommy object (hardcoded address for the arduino)
val = a.get_val() # gets the value thru serial upon request 

'''

from serial.tools import list_ports
import serial
import time


class ArdyCommie:
    def __init__(self):
        self.arduino = serial.Serial(port='/dev/cu.usbmodem101', baudrate=115200, timeout=0.1)
        self.value = None
        
    
    def get_val(self):
        '''
        store the serial info in attribute
        '''
        return self.arduino.readline().decode('utf-8').strip()










