import requests
from requests_oauthlib import OAuth2Session
import json
import win32api
import win32gui
#Windows VirtualKeyCoed
mediaNext = 0xB0
mediaLast = 0xB1
mediaPause = 0xB3

result = None
data = None
authorization_response = None
client_id = "678a44df3488479d97bcd9995f4d419d" # see in Swypad Dashboard
client_secret = "aa5a13cac9b84027a72ce7ad6e36e182" # see in Swypad Dashboard
redirect_uri = "https://lvh.me/" # directs to 127.0.0.1

scope = [ 'user-read-email', 'user-read-birthdate', 'user-read-playback-state', 'user-modify-playback-state', 'user-read-currently-playing', 'app-remote-control']

oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)

authorization_url, state = oauth.authorization_url('https://accounts.spotify.com/authorize', 12345)\

#just needed once (at the start of the program)
def getToken():
    print("Go to: " + authorization_url)
    global  authorization_response
    authorization_response = raw_input('Enter the full callback URL: ')

    oauth.fetch_token(
        'https://accounts.spotify.com/api/token',
        authorization_response=authorization_response,
        client_secret=client_secret)

def getJson():
    global data
    result = oauth.get('https://api.spotify.com/v1/me/player') #returns informations
    data = json.loads(result.text) #convert to json

def getInfo():
    if data != None:
        try:
            items  = data["item"]
            songName = items["name"]
            artist = items["artists"][0]["name"]
            progress = str(data["progress_ms"] / 1000)
            print("Song: " + songName + " Artist: " + str(artist) + " Progress: " + progress)
            return songName,artist,progress
        except:
            oauth.fetch_token(
                'https://accounts.spotify.com/api/token',
                authorization_response=authorization_response,
                client_secret=client_secret)
            return None,None,None

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

