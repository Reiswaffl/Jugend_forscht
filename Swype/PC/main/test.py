import data
import serialPi
import mouseControl
import logic
import time
shortcut = 'ctrl,c'
#mouseControl.handleShortcut("hotkey",shortcut)

reader = data.Reader()
print(reader.getSaves())
print(reader.getShortcut('01'))
print(reader.getCOM ())