from spotify import spotifyAPI
import time
spotifyAPI.getToken()

while 1:
    spotifyAPI.getJson()
    spotifyAPI.getInfo()
    time.sleep(2)