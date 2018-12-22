import xml.etree.ElementTree as ET
import os

path="../resources"

for filename in os.listdir(path):
    if not filename.endswith('.xml'):continue
    fullname = os.path.join(path,filename)
    doc = ET.parse(fullname)
root = doc.getroot()

class Reader:

    def __init__(self):
        for filename in os.listdir(path):
            if not filename.endswith('.xml'): continue
            fullname = os.path.join(path, filename)
            doc = ET.parse(fullname)
        self.root = doc.getroot()

    def getCommand(self,id):
        for child in root:
            if child.get('id') == id:
                return child.get('command')
        return None

    def getShortcut(self,id):
        for child in root:
            if child.get('id') == id:
                return child.text
        return None