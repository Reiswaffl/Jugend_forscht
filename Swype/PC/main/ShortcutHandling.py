import subprocess
import webbrowser
import pyautogui
import mouseControl
import spotify.spotifyAPI as spotifyAPI
import os


def handleShortcut(value):
    if 'O' in value:
        print('open')
        try:
            value = value.replace('O', '')
            open(value)
        except:
            print('failed to find ' + value)
    elif 'W' in value:
        print('website')
        try:
            value = value.replace('W', '')
            openWebsite(value)
        except:
            print('failed to open ' + value)
    else:
        try:
            eval(value)
        except:
            print('failed to run ' + str(value))


def handleSpotShortcut(spotcut):
    try:
        eval(spotcut)
    except:
        print('failed to use ' + spotcut)


def startSpotify():
    spotifyAPI.getToken()
    spotifyAPI.getJson()


def open(path):
    try:
        subprocess.Popen(path)
    except:
        os.startfile(path)
        print('os.startfile')


def openWebsite(url):
    webbrowser.open(url, new=0, autoraise=True)


def copy():
    pyautogui.hotkey('ctrl', 'c')


def paste():
    pyautogui.hotkey('ctrl', 'v')


def cut():
    pyautogui.hotkey('ctrl', 'x')


def takescreen():
    pyautogui.hotkey('win', 'printscreen')


def enter():
    pyautogui.press('enter')


def S(value):
    if value == "+":
        #subprocess.Popen("UP.bat")
        pyautogui.hotkey('volumeup')
        pyautogui.hotkey('volumeup')
        pyautogui.hotkey('volumeup')
    if value == "-":
        #subprocess.Popen("DOWN.bat")
        pyautogui.hotkey('volumedown')
        pyautogui.hotkey('volumedown')
        pyautogui.hotkey('volumedown')


def browserback():
    pyautogui.press('browserback')


def browserforward():
    pyautogui.press('browserforward')


def rightclick():
    mouseControl.rightClick()


def leftclick():
    mouseControl.click()


def holdleftclick():
    mouseControl.leftDown()


def play():
    spotifyAPI.play()


def pause():
    spotifyAPI.pause()


def forward():
    spotifyAPI.nextSong()


def getValue():
    pass


def getVolume():
    return spotifyAPI.getVolume()


def getTitle():
    return spotifyAPI.getTitle()


def getArtist():
    return spotifyAPI.getArtist()


def getProgress():
    return spotifyAPI.getProgess()

def isPlaying(): #bool-value
    return spotifyAPI.isPlaying()
def back():
    spotifyAPI.lastSong()


def getTitlelength():
    pass


def setVolume(v):
    spotifyAPI.setVolume(v)


def getInfo():
    spotifyAPI.getJson()
    return spotifyAPI.getInfo()


def updateJson():
    spotifyAPI.getJson()


def underline():
    pyautogui.hotkey('ctrl', 'shift', 'u')


def bold():
    pyautogui.hotkey('ctrl', 'shift', 'f')


def italic():
    pyautogui.hotkey('ctrl', 'shift', 'k')
