'''
Poll arduino info continuously.
Usage:

a = ArdyCommy() #Initialize an ArdyCommy object (hardcoded address for the arduino)
a.poll_via_thread() # begin the thread for the ardy object to continuously read data

to access the values, you can query a.value at any time 

'''

from serial.tools import list_ports
import serial
import time

import threading

class ArdyCommie:
    def __init__(self):
        self.arduino = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=0.1)
        self.value = None
        
    
    def poll(self):
        '''
        store the serial info in attribute
        '''
        while True:
            self.value = self.arduino.readline().decode('utf-8').strip()
            time.sleep(0.01)

    def poll_via_thread(self):
        thread = threading.Thread(target=self.poll, daemon=True)
        thread.start()







