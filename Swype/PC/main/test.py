import win32api
import spotifyAPI
import time
#Windows VirtualKeyCoed
mediaNext = 0xB0
mediaLast = 0xB1
mediaPause = 0xB3

def hwcode(Media):
	hwcode = win32api.MapVirtualKey(Media, 0)
	return hwcode

def nextSong():
    win32api.keybd_event(mediaNext,hwcode(mediaNext))

def lastSong():
    win32api.keybd_event(mediaLast,hwcode(mediaLast))

def pause():
    win32api.keybd_event(mediaPause,hwcode(mediaPause))

def play():
    win32api.keybd_event(mediaPause,hwcode(mediaPause))

spotifyAPI.getToken()


'''play()
time.sleep(3)
play()
time.sleep(3)
nextSong()
time.sleep(3)
lastSong()'''
