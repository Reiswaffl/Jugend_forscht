import logic
import time
import spotifyAPI

logic = logic.Logic()
logic.start(logic.getCOM())
while True:
    logic.handleInput()
    #logic.spotifyHandling()
    time.sleep(0.0001)
