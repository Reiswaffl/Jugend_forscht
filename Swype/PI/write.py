import serial
import time

ser = serial.Serial(
    port='/dev/ttyAMA0',
    baudrate= 115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)
time.sleep(1)

def write_Shortcut(shortcutNumber):
    ser.write(('SH' +shortcutNumber))

def write_Movement(x,y):
    ser.write(x + ',' + y)

