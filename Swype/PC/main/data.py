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

<<<<<<< HEAD
    def getCOM(self):
        for child in self.root:
            if child.tag == 'COM':
                return child.get('com')
        return None

    def getSaves(self):
=======
    def getCommand(self, id):
>>>>>>> 1ea3d717c570084d0b290468e5fe575a9b4de289
        for child in self.root:
            if child.tag == 'saves':
                return child
        return None
    def getCommand(self,id):
        for child in self.getSaves():
            if child.get('id') == id:
                return child.get('command')
        return None

<<<<<<< HEAD
    def getShortcut(self,id):
        for child in self.getSaves():
=======
    def getShortcut(self, id):
        for child in self.root:
>>>>>>> 1ea3d717c570084d0b290468e5fe575a9b4de289
            if child.get('id') == id:
                return child.text
        return None

<<<<<<< HEAD
    def setCommand(self,id,command):
        for child in self.getSaves():
=======
    def setCommand(self, id, command):
        for child in self.root:
>>>>>>> 1ea3d717c570084d0b290468e5fe575a9b4de289
            if child.get('id') == id:
                child.set('command', command)
                self.doc.write(self.fullname)
                return child.get('command')
        return None

<<<<<<< HEAD
    def setShortcut(self,id, shortcut):
        for child in self.getSaves():
=======
    def setShortcut(self, id, shortcut):
        for child in self.root:
>>>>>>> 1ea3d717c570084d0b290468e5fe575a9b4de289
            if child.get('id') == id:
                child.text = shortcut
                self.doc.write(self.fullname)
                return child.text
        return None

    def setCOM(self,com):
        COM = self.getCOM()
        COM.set('com',com)
