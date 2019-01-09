import logic
import serialPi

ser = serialPi.Ser()
ser.start('COM8')

while 1:
    logic.handleInput()
