import pyautogui
import time
import win32api
import win32con

x = 0
y = 0
z = 0
while z < 40:
    stoptime = time.time()
    pyautogui.moveRel(x, y, 0)
    x += 1
    y += 1
    z += 1
    print(time.time()-stoptime)

print("next part")
time.sleep(1)

x = 0
y = 0
z = 0
while z < 40:
    stoptime = time.time()
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y)
    x += 1
    y += 1
    z += 1
    print(time.time()-stoptime)