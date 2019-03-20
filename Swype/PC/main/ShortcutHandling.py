import subprocess
import webbrowser
import pyautogui
import mouseControl
#import spotify.spotifyAPI as spotifyAPI


def handleShortcut(value):
    if 'O' in value:
        print('open')
        try:
            value.replace('O', '')
            eval(value)
        except:
            print('failed to find ' + value)
    elif 'W' in value:
        print('website')
        try:
            value.replace('W', '')
            openWebsite(value)
        except:
            print('failed to open ' + value)
    else:
        try:
            eval(value)
        except:
            print('failed to run ' + value)


def handleSpotShortcut(spotcut):
    try:
        eval(spotcut)
    except:
        print('failed to use ' + spotcut)


def open(path):
    subprocess.Popen(path)


def openWebsite(url):
    webbrowser.open(url, new=0, autoraise=True)


def copy():
    pyautogui.hotkey('str', 'c')


def paste():
    pyautogui.hotkey('str', 'v')


def cut():
    pyautogui.hotkey('str', 'x')


def takescreen():
    pyautogui.hotkey('win', 'printscreen')


def enter():
    pyautogui.press('enter')


def S(value):
    if value == "+":
        subprocess.Popen("UP.bat")
    if value == "-":
        subprocess.Popen("DOWN.bat")


def browserback():
    pyautogui.press('browserback')


def brwoserforward():
    pyautogui.press('brwoserforward')


def rightclick():
    mouseControl.rightDown()


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
    pass


def getTitle():
    pass


def back():
    spotifyAPI.lastSong()


def getTitlelength():
    pass


def setVolume(v):
    pass
