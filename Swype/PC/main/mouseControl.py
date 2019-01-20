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
        pyautogui.moveTo(x + int(xMovement), y + int(yMovement), speed, pyautogui.easeOutQuad)
    except:
        pass

def hotkey(shortcut):
    try:
        sh = shortcut.split(',')
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