import xml.etree.ElementTree as ET
import os

path = "../resources"


class Reader:

    def __init__(self):
        for filename in os.listdir(path):
            if not filename.endswith('.xml'):
                continue
            self.fullname = os.path.join(path, filename)
            self.doc = ET.parse(self.fullname)
        self.root = self.doc.getroot()

    def getSpecificShortcut(self, id):
        for child in self.root:
            if child.tag == 'shortcut':
                return child.get(id)
        return None

    def getSSHbyTag(self, tag):
        for child in self.getShortcuts():
            if child.get('command') == tag:
                return child
        return None

    def getShortcuts(self):
        for child in self.root:
            if child.tag == 'shortcuts':
                return child
        return None

    def setShortcut(self, id, value):
        for child in self.getShortcuts():
            if child.get('id') == id:
                child.text = value
                self.doc.write(self.fullname)
                return child
        return None

    def getSpecificSpotifyShortcut(self, id):
        for child in self.getSpotifyShortcuts():
            if child.get('id') == id:
                return child
        return

    def getSSSbyTag(self, tag):
        for child in self.getSpotifyShortcuts():
            if child.get('command') == tag:
                return child
        return None

    def getSpotifyShortcuts(self):
        for child in self.root:
            if child.tag == 'spotify':
                return child
        return None

    def setSpotifyShortcut(self, id, value):
        for child in self.getSpotifyShortcuts():
            if child.get('id') == id:
                child.text = value
                self.doc.write(self.fullname)
                return child
        return None

    def getCOM(self):
        for child in self.root:
            if child.tag == 'COM':
                return child.get('com')
        return None

    def getSaves(self):
        for child in self.root:
            if child.tag == 'saves':
                return child
        return None

    def getCommand(self, id):
        for child in self.getSaves():
            if child.get('id') == id:
                print("triggered")
                return child.get('command')
        return None

    def getShortcut(self, id):
        for child in self.getSaves():
            if child.get('id') == id:
                return child.text
        return None

    def setCommand(self, id, command):
        for child in self.getSaves():
            if child.get('id') == id:
                child.set('command', command)
                self.doc.write(self.fullname)
                return child.get('command')
        return None

    '''def setShortcut(self, id, shortcut):
        for child in self.getSaves():
            if child.get('id') == id:
                child.text = shortcut
                self.doc.write(self.fullname)
                return child.text
        return None'''

    def setCOM(self, com):
        for child in self.root:
            if child.tag == 'COM':
                child.set('com', com)
                self.doc.write(self.fullname)
