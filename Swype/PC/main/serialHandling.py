import logic
import time
import spotifyAPI
last = time.time()
counter = 0
progress = 0
lastname = None
logic = logic.Logic()
logic.start(logic.getCOM())
spotifyAPI.getToken()
while True:
    logic.handleInput()
    if time.time() - last > 1:
        #one second passed
        last = time.time()
        logic.sendTime(progress+counter)
        counter += 1
        if counter >= 5:
            spotifyAPI.getJson()
            song, artist, progress = spotifyAPI.getInfo()
            counter = 0
            if song != lastname:
                logic.sendAll(song,artist,progress)
            else:
                logic.sendTime(progress)
    time.sleep(0.0001)
