import data
import serialPi
import mouseControl

serial = serialPi.Ser()
serial.start('com10')
reader = data.Reader()
def handleInput(incoming_data):
    #incoming_data = serial.getIncomingData()
    if ',' in incoming_data:
        #mouse movement
        x,y = incoming_data.split(',')
        mouseControl.handleMouse(x,y,0.4) #0.4 as default now, maybe change later
    if '!' in incoming_data:
        #shortcut
        id = incoming_data.replace('!','')
        command = reader.getCommand(id)
        shortcut  = reader.getShortcut(id)
        mouseControl.handleShortcut(command,shortcut)