import data
import serialPi
import mouseControl

serial = serialPi.Ser()
reader = data.Reader()
mouseSpeed = 1.7
click = 0


class Logic:

    def __init__(self):
        self.clickcounter = 0

    def start(self, com):
        return serial.start(com)

    def handleInput(self):
        incoming_data = serial.getIncomingData()
        print(incoming_data)
        if ',' in incoming_data:
            # mouse movement
            movement = incoming_data.replace('\n', '')
            x, y = movement.split(',')
            mouseControl.handleMouse(x, y, mouseSpeed)
        if '!' in incoming_data:
            # shortcut
            id = incoming_data.replace('!', '')
            id = id.replace(' ', '')
            id = id.replace('\n', '').replace('\r', '')
            command = reader.getCommand(id)
            shortcut = reader.getShortcut(id)
            mouseControl.handleShortcut(command, shortcut)
        if 'n' in incoming_data:
            key = incoming_data.replace('n', '')
            key = key.replace("\n", '').replace('\r', '')
            mouseControl.numPad(key)
        if 's' in incoming_data:
            print(incoming_data + "step 2")
            value = incoming_data.replace("\n", '').replace('\r', '').replace(' ', '')
            mouseControl.volume(value)

        if 'c1' in incoming_data:  # left click
            if self.clickcounter > 0:
                mouseControl.click()
                print("left click")
                self.clickcounter = 0
            else:
                self.clickcounter += 1
            # mouseControl.releaseAll()
        if 'c2' in incoming_data:  # right click
            mouseControl.rightDown()
            # mouseControl.releaseAll()
            print("right click")
        if 'c3' in incoming_data:  # left mouse down
            mouseControl.leftDown()
        if 'r' in incoming_data:  # release all mouse buttons
            mouseControl.releaseAll()

    def writeShortcut(self, id, command, shortcut):
        reader.setCommand(id, command)
        reader.setShortcut(id, shortcut)

    def getCOM(self):
        return reader.getCOM()

    def setCOM(self, com):
        reader.setCOM(com)

    def getShortCut(self, id):
        return reader.getCommand(id), reader.getShortcut(id)

    def sendTime(self,time):
        serial.write(time)

    def sendAll(self,song,artist,time):
        serial.write(song + ',' + artist + ',' + time)