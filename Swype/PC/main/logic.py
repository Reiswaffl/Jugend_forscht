import data
import serialPi
import mouseControl


serial = serialPi.Ser()
reader = data.Reader()
mouseSpeed = 0.4


def start(com):
     serial.start(com)


def handleInput():
    incoming_data =  serial.getIncomingData()
    if ',' in incoming_data:
        # mouse movement
        x,y = incoming_data.split(',')
        mouseControl.handleMouse(x,y,mouseSpeed) # 0.4 as default now, maybe change later
    if '!' in incoming_data:
        # shortcut
        id = incoming_data.replace('!','')
        command = reader.getCommand(id)
        shortcut = reader.getShortcut(id)
        mouseControl.handleShortcut(command,shortcut)

def writeShortcut(id,command,shortcut):
    reader.setCommand(id,command)
    reader.setShortcut(id,shortcut)
def getCOM():
    return reader.getCOM()

def setCOM(com):
    reader.setCOM(com)
def getShortCut(id):
    return reader.getCommand(id), reader.getShortcut(id)