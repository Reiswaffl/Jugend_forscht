import pyautogui
import time
def move(xMovement,yMovement):
    x,y = pyautogui.position()
    pyautogui.moveTo(x+xMovement,y+yMovement,0.4,pyautogui.easeOutQuad)

move(100,100)
time.sleep(1)
move(100,-100)
time.sleep(1)
move(-100,100)
time.sleep(1)
move(-100,-100)
time.sleep(1)