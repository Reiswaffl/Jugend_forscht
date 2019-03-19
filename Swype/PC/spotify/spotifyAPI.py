import requests
from requests_oauthlib import OAuth2Session
import json
import win32api
import win32gui
import time

# Windows VirtualKeyCoed
mediaNext = 0xB0
mediaLast = 0xB1
mediaPause = 0xB3

result = None
data = None
authorization_response = None
client_id = "678a44df3488479d97bcd9995f4d419d"  # see in Swypad Dashboard
client_secret = "aa5a13cac9b84027a72ce7ad6e36e182"  # see in Swypad Dashboard
redirect_uri = "https://lvh.me/"  # directs to 127.0.0.1
crashed = False
scope = ['user-read-email', 'user-read-birthdate', 'user-read-playback-state', 'user-modify-playback-state',
         'user-read-currently-playing', 'app-remote-control']

oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)

authorization_url, state = oauth.authorization_url('https://accounts.spotify.com/authorize', 12345) \
 \
 \
# just needed once (at the start of the program)
def getToken():
    print("Go to: " + authorization_url)
    global authorization_response
    authorization_response = raw_input('Enter the full callback URL: ')

    oauth.fetch_token(
        'https://accounts.spotify.com/api/token',
        authorization_response=authorization_response,
        client_secret=client_secret)


def getJson():
    if not crashed:
        global data
        result = oauth.get('https://api.spotify.com/v1/me/player')  # returns informations
        data = json.loads(result.text)  # convert to json


def getInfo():
    global crashed
    if data != None and crashed == False: # crashed == True if SpotifyAPI breaks
        try:
            items = data["item"]
            songName = items["name"]
            artist = items["artists"][0]["name"]
            progress = str(data["progress_ms"] / 1000)
            volume = data["device"]["volume_percent"]
            print("Song: " + songName + " Artist: " + str(artist) + " Progress: " + progress + " Volume in percent: " + volume)
            return songName, artist, progress, volume
        except:
            try:
                oauth.fetch_token(
                    'https://accounts.spotify.com/api/token',
                    authorization_response=authorization_response,
                    client_secret=client_secret)
                return None, None, None
            except:
                crashed = True
    else: # SpotifyAPI broke
        get_info_windows()


def hwcode(Media):
    hwcode = win32api.MapVirtualKey(Media, 0)
    return hwcode


def nextSong():
    win32api.keybd_event(mediaNext, hwcode(mediaNext))


def lastSong():
    win32api.keybd_event(mediaLast, hwcode(mediaLast))


def pause():
    win32api.keybd_event(mediaPause, hwcode(mediaPause))


def play():
    win32api.keybd_event(mediaPause, hwcode(mediaPause))
def get_info_windows():
    windows = []



    # Newer Spotify versions - create an EnumHandler for EnumWindows and flood the list with Chrome_WidgetWin_0s
    def find_spotify_uwp(hwnd, windows):
        text = win32gui.GetWindowText(hwnd)
        if win32gui.GetClassName(hwnd) == "Chrome_WidgetWin_0" and len(text) > 0:
            windows.append(text)

    win32gui.EnumWindows(find_spotify_uwp, windows)
    print('Starting shit')
    while windows.count != 0:
        try:
            text = windows.pop()
            print(text)
        except:
            return "Error", "Nothing playing"
        try:
            artist, track = text.split(" - ", 1)
            print( artist, track )
        except:
            print('Error')
getToken()
while(1):
    getJson()
    print(getInfo())
    time.sleep(2)