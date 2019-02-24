import logic
import time

logic = logic.Logic()
logic.start(logic.getCOM())
while 1:
    logic.handleInput()
    time.sleep(0.0001)
