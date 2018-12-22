import data
import serialPi
import mouseControl

serial = serialPi.Ser()
serial.start()
def handleInput():
    incoming_data = serial.getIncomingData()
    if ',' in incoming_data:
        #mouse movement
        mouseControl.handleMouse()
    else:
        #shortcut
        x,y = incoming_data.split(',')
        mouseControl.handleShortcut(x,y,0.4) #0.4 as default now, maybe change later