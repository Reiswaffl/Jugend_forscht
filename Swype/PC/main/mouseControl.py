import pyautogui

def handleShortcut(command, shortcut):
    pyautogui.hotkey(shortcut.split(","))

def handleMouse(xMovement,yMovement,speed):
    x,y = pyautogui.position()
    pyautogui.moveTo(x + int(xMovement), y + int(yMovement), speed, pyautogui.easeOutQuad)
