import logic
import time
import spotifyAPI
last = time.time()
lastname = None
logic = logic.Logic()
logic.start(logic.getCOM())
spotifyAPI.getToken()
while True:
    logic.handleInput()
    if time.time() - last > 1:
        #one second passed
        last = time.time()
        spotifyAPI.getJson()
        song, artist, progress = spotifyAPI.getInfo()
        if song != lastname:
            logic.sendAll(song,artist,progress)
        else:
            logic.sendTime(progress)
    time.sleep(0.0001)
