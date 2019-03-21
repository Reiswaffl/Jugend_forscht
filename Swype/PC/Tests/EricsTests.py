import serial
import time
com = "COM8"
Pi_Serial = serial.Serial(com, 115200, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)
time.sleep(1)

if Pi_Serial.isOpen():  # opens it again, if its open already (to minimize error rate)
    Pi_Serial.close()
    Pi_Serial.open()

while 1:
    Pi_Serial.write("Hello World")
    time.sleep(5);