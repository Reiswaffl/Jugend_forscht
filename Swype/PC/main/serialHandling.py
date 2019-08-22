import logic
import time

last = time.time()
counter = 0
progress = 0
lastname = None
logic = logic.Logic()
logic.start(logic.getCOM())
while True:
    # print("Running")
    logic.inputHandling()
    '''try:
        if time.time() - last > 1:

            # one second passed
            last = time.time()
            #logic.sendTime(progress + counter)
            print(progress)
            counter += 1
            if counter >= 5:
                song, artist, progress = logic.getSpotifyInfo()
                counter = 0
                if song != lastname:
                    #logic.sendAll(song, artist, progress)
                    print(song,artist,progress)
                    lastname = song
                else:
                    print(progress)
                    #logic.sendTime(progress)\'
                    
    except:
        print('Didnt work') '''
    time.sleep(0.0001)
