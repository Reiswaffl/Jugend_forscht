import pyautogui
import subprocess

def handleShortcut(command, shortcut):
    if command == 'hotkey':
        hotkey(shortcut)
    if command == 'scroll':
        scroll(shortcut)
    if command == 'program':
        runProgramm(shortcut)

def handleMouse(xMovement, yMovement, speed):
    try:
        x, y = pyautogui.position()
        pyautogui.moveTo(x + int(xMovement), y + int(yMovement))
    except:
        pass

def hotkey(shortcut):
    try:
        sh = shortcut.split('+')
        print(sh)
        if len(sh) == 2:
            pyautogui.hotkey(sh[0], sh[1])
        if len(sh) == 3:
            pyautogui.hotkey(sh[0], sh[1], sh[2])
        if len(sh) == 4:
            pyautogui.hotkey(sh[0], sh[1], sh[2], sh[3])
    except:
        pass

def scroll(shortcut):
    try:
        i = shortcut.replace('i', '')
        pyautogui.scroll(int(i))
    except:
        pass

def runProgramm(path):
    try:
        subprocess.Popen([path])
    except:
        pass

def numPad(key):
    try:
        pyautogui.keyDown(key)
        pyautogui.keyUp(key)
    except:
        pass

def leftDown():
    try:
        pyautogui.mouseDown()
    except:
        pass

def rightDown():
    try:
        pyautogui.mouseDown(button='right')
    except:
        pass

def releaseAll():
    try:
        pyautogui.mouseUp(button='right')
        pyautogui.mouseUp()
    except:
        pass