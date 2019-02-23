import data
import serialPi
import mouseControl


serial = serialPi.Ser()
reader = data.Reader()
mouseSpeed = 0.4


def start(com):
     return serial.start(com)


def handleInput():
    incoming_data = serial.getIncomingData()
    #print(incoming_data)
    if ',' in incoming_data:
        # mouse movement
        movement = incoming_data.replace('\n', '')
        x,y = movement.split(',')
        #incoming_data.replace('\n', '')
        mouseControl.handleMouse(x,y,mouseSpeed) # 0.4 as default now, maybe change later
    if '!' in incoming_data:
        # shortcut
        id = incoming_data.replace('!','')
        id = id.replace(' ','')
        id = id.replace('\n','').replace('\r','')
        command = reader.getCommand(id)
        shortcut = reader.getShortcut(id)
        mouseControl.handleShortcut(command,shortcut)
    if 'n' in incoming_data:
        key = incoming_data.replace('n', '')
        key = key.replace("\n", '').replace('\r','')
        mouseControl.numPad(key)
    if 's' in incoming_data:
        value = incoming_data.replace("\n", '').replace('\r','').replace(' ','')
        mouseControl.volume(value)

    if 'c1' in incoming_data:   #leftclick
        mouseControl.click()
    if 'c2' in incoming_data:   #rightclick
        mouseControl.rightDown()
        mouseControl.releaseAll()
    if 'c3' in incoming_data:   #left mouse down
        mouseControl.leftDown()
    if 'r' in incoming_data:    #release all mousebuttons
        mouseControl.releaseAll()
def writeShortcut(id,command,shortcut):
    reader.setCommand(id,command)
    reader.setShortcut(id,shortcut)
def getCOM():
    return reader.getCOM()

def setCOM(com):
    reader.setCOM(com)
def getShortCut(id):
    return reader.getCommand(id), reader.getShortcut(id)