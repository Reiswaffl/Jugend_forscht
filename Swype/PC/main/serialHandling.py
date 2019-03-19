import logic
import time
import spotify.spotifyAPI


logic = logic.Logic()
logic.start(logic.getCOM())
while True:
    logic.handleInput()
    #logic.spotifyHandling()
    time.sleep(0.0001)
