import pyautogui
import time
import win32api
import win32con

time.sleep(1)
print('go')

win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
time.sleep(1)

win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
time.sleep(1)

#win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
#win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
#time.sleep(1)

#win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
#win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
