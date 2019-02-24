import time

import pyautogui
import subprocess
import win32con
import win32api

leftup = True
rightup = True
lasttime = time.time()


def handleShortcut(command, shortcut):
    #print(command, shortcut)
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
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(int(xMovement)*speed), int(int(yMovement)*speed))
    except:
        print("mouse movement failed")
        print(int(xMovement)*speed, xMovement, speed)


def hotkey(shortcut):
    global lasttime
    try:
        if time.time() > lasttime + 1:
            sh = shortcut.split('+')
            print(sh)
            if len(sh) == 2:
                pyautogui.hotkey(sh[0], sh[1])
            if len(sh) == 3:
                pyautogui.hotkey(sh[0], sh[1], sh[2])
            if len(sh) == 4:
                pyautogui.hotkey(sh[0], sh[1], sh[2], sh[3])
            lasttime = time.time()
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
    global leftup
    try:
        if leftup:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            leftup = False
        #if not leftup:
         #   win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
          #  leftup = True
        #pyautogui.mouseDown(button='left')
        #pyautogui.mouseDown(button='left')
    except:
        print("click failed")
        pass
    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def leftDown():
    global leftup
    try:
        if leftup:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            leftup = False
        #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP)
        #pyautogui.mouseDown(button='left')
    except:
        pass


def rightDown():
    global rightup
    try:
        if rightup:
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
            rightup = False
        #if not rightup:
         #   win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
          #  rightup = True
        #pyautogui.mouseDown(button='right')
        #pyautogui.mouseUp(button='right')
    except:
        pass


def releaseAll():
    global leftup
    global rightup
    try:
        if not rightup:
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
            rightup = True
        if not leftup:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            leftup = True
        #pyautogui.mouseUp(button='right')
        #pyautogui.mouseUp(button='left')
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
