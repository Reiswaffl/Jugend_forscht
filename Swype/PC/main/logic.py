import dataWriterReader
import serialPi
import mouseControl
import time
import ShortcutHandling
serial = serialPi.Ser()
reader = dataWriterReader.Reader()
mouseSpeed = 1.7
click = 0


class Logic:
    last = 0
    counter = 0
    progress = 0
    lastname = 0

    def __init__(self):
        self.clickcounter = 0

    def start(self, com):
        return serial.start(com)

    def inputHandling(self):
        incoming_data = serial.getIncomingData()
        print(incoming_data)
        if 'M' in incoming_data:
            print('M')
            global mouseSpeed
            movement = incoming_data.replace('\n', '').replace('M', '')
            x, y = movement.split(',')
            mouseControl.handleMouse(x, y, mouseSpeed)
        elif 'W' in incoming_data:
            print('W')
            key = incoming_data.replace('\n', '').replace('W', '')
            mouseControl.write(key)
        elif 'R' in incoming_data:
            print('R')
            mouseControl.releaseAll()
        elif 'SC' in incoming_data:
            sc = incoming_data.replace('\n', '').replace('SC', '')
            shortcut = reader.getSSHbyTag(sc).text
            ShortcutHandling.handleShortcut(shortcut)
            print(shortcut)
        elif 'SP' in incoming_data:
            sp = incoming_data.replace('\n', '').replace('SP', '').replace('\r','')
            spotcommand = reader.getSSSbyTag(sp)
            ShortcutHandling.handleSpotShortcut(spotcommand)
            print spotcommand
        elif 'S' in incoming_data:
            print('S')
            volume = incoming_data.replace('\n', '').replace('S', '')
            mouseControl.volume(volume)

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

    def getSpotifyInfo(self):
        return ShortcutHandling.getInfo()

    def sendTime(self, time):
        serial.write(time)

    def sendAll(self, song, artist, time):
        serial.write(song + ',' + artist + ',' + time)
