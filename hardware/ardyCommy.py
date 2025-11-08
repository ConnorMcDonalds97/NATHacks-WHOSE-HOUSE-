from serial.tools import list_ports
import serial
import time


arduino = serial.Serial(port='/dev/cu.usbmodem101', baudrate=115200, timeout=0.1)

def write_read(x):
    #arduino.write(bytes(x,'utf-8'))
    time.sleep(1)
    data = arduino.readline()
    return data

while True:
    value = write_read(1)
    value = int.from_bytes(value)
    print(value)




