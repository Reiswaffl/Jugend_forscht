import logic
import serialPi


logic.start(logic.getCOM())
while 1:
    logic.handleInput()
