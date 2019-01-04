import data
# import serialPi
import mouseControl
import userInterface

<<<<<<< HEAD
serial = serialPi.Ser()
reader = data.Reader()
mouseSpeed = 0.4
def start(com):
    serial.start(com)
def handleInput():
    incoming_data = serial.getIncomingData()
    if ',' in incoming_data:
        #mouse movement
        x,y = incoming_data.split(',')
        mouseControl.handleMouse(x,y,mouseSpeed) #0.4 as default now, maybe change later
=======
# serial = serialPi.Ser()
# serial.start('com10')
reader = data.Reader()
interface = userInterface.userInterface()
interface.buildInterface()
interface.mainloop()


def handleInput(incoming_data):
    # incoming_data = serial.getIncomingData()
    if ',' in incoming_data:
        # mouse movement
        x, y = incoming_data.split(',')
        mouseControl.handleMouse(x, y, 0.4) # 0.4 as default now, maybe change later
>>>>>>> 1ea3d717c570084d0b290468e5fe575a9b4de289
    if '!' in incoming_data:
        # shortcut
        id = incoming_data.replace('!','')
        command = reader.getCommand(id)
        shortcut = reader.getShortcut(id)
        mouseControl.handleShortcut(command,shortcut)