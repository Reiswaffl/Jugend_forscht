import pyautogui

def handleShortcut(command, shortcut):
    if command == 'hotkey':
        hotkey(shortcut)
    if command == 'scroll':
        scroll(shortcut)

def handleMouse(xMovement,yMovement,speed):
    x,y = pyautogui.position()
    pyautogui.moveTo(x + int(xMovement), y + int(yMovement), speed, pyautogui.easeOutQuad)


def hotkey(shortcut):
    pyautogui.hotkey(shortcut.split(','))

def scroll(shortcut):
    i = shortcut.replace('i','')
    pyautogui.scroll(int(i))