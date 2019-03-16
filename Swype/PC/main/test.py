import spotifyAPI
import time

spotifyAPI.getToken()
while 1:
    spotifyAPI.getJson()
    print(spotifyAPI.getInfo())
    time.sleep(1)