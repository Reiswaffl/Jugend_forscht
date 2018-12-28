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
    sh = shortcut.split(',')
    if len(sh) == 2:
        pyautogui.hotkey(sh[0],sh[1])
    if len(sh) == 3:
        pyautogui.hotkey(sh[0],sh[1],sh[2])
    if len(sh) == 4:
        pyautogui.hotkey(sh[0],sh[1],sh[2],sh[3])

def scroll(shortcut):
    i = shortcut.replace('i','')
    pyautogui.scroll(int(i))