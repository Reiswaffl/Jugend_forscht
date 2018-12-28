import data
import serialPi
import mouseControl
import logic
import time
shortcut = 'ctrl,c'
#mouseControl.handleShortcut("hotkey",shortcut)

time.sleep(3)
logic.handleInput('!01')
logic.handleInput('!02')
logic.handleInput('!01')
logic.handleInput('!02')
logic.handleInput('!01')
logic.handleInput('!02')
logic.handleInput('!01')
logic.handleInput('!02')

