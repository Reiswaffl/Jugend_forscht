import pyautogui
import subprocess
import win32con
import win32api


def handleShortcut(command, shortcut):
    if command == 'hotkey':
        hotkey(shortcut)
    if command == 'scroll':
        scroll(shortcut)
    if command == 'program':
        runProgramm(shortcut)


def handleMouse(xMovement, yMovement, speed):
    try:
        # x, y = pyautogui.position()
        # pyautogui.moveTo(x + int(xMovement), y + int(yMovement), 0)
        # pyautogui.moveRel(int(xMovement), int(yMovement), 0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(xMovement), int(yMovement))
    except:
        print("mouse movement failed")


def hotkey(shortcut):
    print(shortcut)
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


def click():
    try:
        pyautogui.click()
    except:
        pass


def leftDown():
    try:
        pyautogui.mouseDown(button='left')
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
        pyautogui.mouseUp(button='left')
    except:
        pass  #


def volume(value):
    try:
        if value == "s+":
            subprocess.Popen("UP.bat")
        if value == "s-":
            subprocess.Popen("DOWN.bat")
    except:
        pass
