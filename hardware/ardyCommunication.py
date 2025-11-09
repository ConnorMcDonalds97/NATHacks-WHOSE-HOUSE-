from serial.tools import list_ports
import serial
import time



# def readHand(portName):
#     '''
#     Function that reads in input from Arduino's flex sensors
#     input: Port name (str)
#     output: A 4 digit int, where each digit is a boolean between 2 (false) and 1 (true)
#             A value of 1 means the corresponding flex sensor is flexed, otherwise 2.
#     '''

#     line = arduino.readline().decode('utf-8').strip()
#     while True:
#         if line:
#             try:
#                 value = int(line)
#                 print("Output:", value)
#             except ValueError:
#                 print("Invalid data:", line)



arduino = serial.Serial(port='/dev/cu.usbmodem101', baudrate=115200, timeout=0.1)



def readHand():
    '''
    Function that reads in input from Arduino's flex sensors
    input: Port name (str)
    output: Writes a 4 digit int into a text file, where each digit is a boolean between 
            2 (false) and 1 (true).
            A value of 1 means the corresponding flex sensor is flexed, otherwise 2.
    '''
    while True:        
        line = arduino.readline().decode('utf-8').strip()
        if line:
            try:
                with open('outputFile.txt', 'w') as file:
                    file.write(line)
            except ValueError:
                print("Invalid data:", line)

# readHand('/dev/cu.usbmodem101')

readHand()


