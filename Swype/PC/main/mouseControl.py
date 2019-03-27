import time
import pyautogui
import subprocess
import win32con
import win32api

leftup = True
rightup = True
lasttime = time.time()


def handleMouse(xMovement, yMovement, speed):
    try:
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(int(xMovement) * speed), int(int(yMovement) * speed))
    except:
        print("mouse movement failed")
        print(int(xMovement) * speed, xMovement, speed)


def scroll(shortcut):
    try:
        i = shortcut.replace('i', '')
        pyautogui.scroll(int(i))
    except:
        pass


def numPad(key):
    try:
        pyautogui.keyDown(key)
        pyautogui.keyUp(key)
    except:
        pass


def write(key):
    try:
        pyautogui.keyDown(key)
        pyautogui.keyUp(key)
    except:
        pass


def click():
    global leftup
    if leftup:
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        leftup = False
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        leftup = True
    #except:
     #   print("click failed")
      #  pass


def leftDown():
    global leftup
    try:
        if leftup:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            leftup = False
    except:
        pass


def rightClick():
    global rightup
    try:
        if rightup:
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
            rightup = False
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
            rightup = True
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
    except:
        pass


def volume(value):
    try:
        if value == "+":
            subprocess.Popen("UP.bat")
        if value == "-":
            subprocess.Popen("DOWN.bat")
    except:
        pass
