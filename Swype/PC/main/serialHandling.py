import logic
import serialPi
import time


logic.start(logic.getCOM())
while 1:
    logic.handleInput()
    time.sleep(0.0001)

