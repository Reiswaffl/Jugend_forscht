# gesture control python program for controlling certain functions in windows pc
# Code by BalaAppu
# Website: www.electronicshub.org

import serial  # add Serial library for serial communication
import pyautogui  # add pyautogui library for programmatically controlling the mouse and keyboard.
import sys

print "Start"
Arduino_Serial = serial.Serial('com10', 9600)  # Initialize serial and Create Serial port object called Arduino_Serial

while 1:
    incoming_data = str(Arduino_Serial.readline())  # read the serial data and print it as line
    print incoming_data  # print the incoming Serial data
    print "HI"
    if 'next' in incoming_data:  # if incoming data is 'next'
        pyautogui.hotkey('ctrl', 'pgdn')  # perform "ctrl+pgdn" operation which moves to the next tab

    if 'previous' in incoming_data:  # if incoming data is 'previous'
        pyautogui.hotkey('ctrl', 'pgup')  # perform "ctrl+pgup" operation which moves to the previous tab

    if 'down' in incoming_data:  # if incoming data is 'down'
        # pyautogui.press('down')                   # performs "down arrow" operation which scrolls down the page
        pyautogui.scroll(-100)

    if 'up' in incoming_data:  # if incoming data is 'up'
        try:
            x,y = pyautogui.position();
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print positionStr
            print '\b' * (len(positionStr) + 2),
            sys.stdout.flush()
        except KeyboardInterrupt:
            print '\n'
        pyautogui.moveTo(100,100)

    if 'change' in incoming_data:  # if incoming data is 'change'
        pyautogui.keyDown('alt')  # performs "alt+tab" operation which switches the tab
        pyautogui.press('tab')
        pyautogui.keyUp('alt')

    incoming_data = "";  # clears the data