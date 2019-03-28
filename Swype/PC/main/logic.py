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
            #print('M')
            global mouseSpeed
            movement = incoming_data.replace('\n', '').replace('M', '')
            x, y = movement.split(',')
            mouseControl.handleMouse(x, y, mouseSpeed)
        elif 'W' in incoming_data:
            #print('W')
            key = incoming_data.replace('\n', '').replace('W', '')
            mouseControl.write(key)
        elif 'R' in incoming_data:
            #print('R')
            mouseControl.releaseAll()
        elif 'SC' in incoming_data:
            sc = incoming_data.replace('\n', '').replace('SC', '')
            shortcut = reader.getSSHbyTag(sc).text
            ShortcutHandling.handleShortcut(shortcut)
            print(shortcut)
        elif 'SP' in incoming_data:
            sp = incoming_data.replace('\n', '').replace('SP', '').replace('\r', '')
            spotcommand = reader.getSSSbyTag(sp)
            ShortcutHandling.handleSpotShortcut(spotcommand)
            #print spotcommand
        elif 'S' in incoming_data:
            #print('S')
            volume = incoming_data.replace('\n', '').replace('S', '')
            mouseControl.volume(volume)

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
