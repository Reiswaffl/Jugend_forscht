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

    def getCommand(self, id):
        for child in self.root:
            if child.get('id') == id:
                return child.get('command')
        return None

    def getShortcut(self, id):
        for child in self.root:
            if child.get('id') == id:
                return child.text
        return None

    def setCommand(self, id, command):
        for child in self.root:
            if child.get('id') == id:
                child.set('command', command)
                self.doc.write(self.fullname)
                return child.get('command')
        return None

    def setShortcut(self, id, shortcut):
        for child in self.root:
            if child.get('id') == id:
                child.text = shortcut
                self.doc.write(self.fullname)
                return child.text
        return None