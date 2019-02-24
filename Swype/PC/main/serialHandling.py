import logic
import time

logic = logic.Logic()
logic.start(logic.getCOM())
while True:
    logic.handleInput()
    time.sleep(0.0001)
