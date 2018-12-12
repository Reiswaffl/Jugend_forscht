import serial
import time
import pyautogui
import sys
print "start"

speed = 0.4
Pi_Serial = serial.Serial('com8',115200,serial.EIGHTBITS,serial.PARITY_NONE,serial.STOPBITS_ONE)
time.sleep(1)

def splitXY(str1):
    xy = str1.split(",")
    return xy

def move(xMovement,yMovement):
    x,y = pyautogui.position()
    pyautogui.moveTo(x+int(xMovement),y+int(yMovement),speed,pyautogui.easeOutQuad)


if Pi_Serial.isOpen():
    Pi_Serial.close()
    Pi_Serial.open()
while True:
    incoming_data = str(Pi_Serial.readline())
    print incoming_data
    if "," in incoming_data:  # "," only allowed in positions-statements
        x,y = splitXY(incoming_data)  #splits String into x- and y-movement
        move(x,y)  #moves mouse
    else: #shortcuts
        if 'next' in incoming_data:  # if incoming data is 'next'
            pyautogui.hotkey('ctrl', 'pgdn')  # perform "ctrl+pgdn" operation which moves to the next tab

        if 'previous' in incoming_data:  # if incoming data is 'previous'
            pyautogui.hotkey('ctrl', 'pgup')  # perform "ctrl+pgup" operation which moves to the previous tab

        if 'down' in incoming_data:  # if incoming data is 'down'
            # pyautogui.press('down')                   # performs "down arrow" operation which scrolls down the page
            pyautogui.scroll(-100)

        if 'up' in incoming_data:  # if incoming data is 'up'
            # pyautogui.press('up')                      # performs "up arrow" operation which scrolls up the page
            pyautogui.scroll(100)

        if 'change' in incoming_data:  # if incoming data is 'change'
            pyautogui.keyDown('alt')  # performs "alt+tab" operation which switches the tab
            pyautogui.press('tab')
            pyautogui.keyUp('alt')

        if 'copy' in incoming_data: #if incoming data is 'copy'
            pyautogui.keyDown('ctrl') #performs "ctrl+copy" operation which copies an object
            pyautogui.press('c')
            pyautogui.keyUp('ctrl')

        if 'paste' in incoming_data: #if incoming data is 'paste'
            pyautogui.keyDown('ctrl') #perform "ctrl+paste" operation which pastes an object
            pyautogui.press('v')
            pyautogui.keyUp('ctrl')
    incoming_data = ""  # clears the data


