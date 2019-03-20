# encoding=utf-8
# import RPi.GPIO as GPIO
from kivy.uix.screenmanager import Screen
from writerScript import *

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
print("GPIO setup done")


def reset():
    global touch, touchcounter, lasttime, dx, dy, ompx, ompy, nmpx, nmpy, start, leftclick, released, end, double, \
        delta, delta2, hold
    touch = False
    touchcounter = 0
    lasttime = 0
    dx = 0
    dy = 0
    ompx = 0
    ompy = 0
    nmpx = 0
    nmpy = 0
    start = time.time()
    leftclick = False
    released = True
    end = time.time()
    double = time.time()
    delta = 0.1
    delta2 = 0.2
    hold = False


reset()


def on_touch_down(self, touch, Screen):
    global touchcounter, start, double, delta2, hold
    touchcounter += 1
    start = time.time()
    if start - double < delta2:
        hold = True
    if True:  # GPIO.input(40):
        if super(Screen, self).on_touch_down(touch):
            return True
        if not self.collide_point(*touch.pos):
            return False


def on_touch_move(self, touch, Screen):
    global end, start, delta2, hold, dx, dy
    end = time.time()  # GPIO.input(40) == False and
    if not True:
        if end - start > delta2:
            touch_input = touch.pos
            calculate_dx_dy(touch_input[0], touch_input[1])
            if hold:
                pass
            # linksklick gedrückt halten
            # send("c3")
            # self.send(0)
            else:
                write_Movement(dx, dy)
            # self.send(0)  # Mausbewegung abgreifen
    else:  # GPIO.input(40):
        if super(Screen, self).on_touch_down(touch):
            return True
        if not self.collide_point(*touch.pos):
            return False


def on_touch_up(self, touch, Screen):
    global end, touchcounter, start, delta, double, hold, leftclick
    end = time.time()
    if touchcounter > 1:
        leftclick = False
    if end - start < delta and touchcounter == 2:
        write_Shortcut("rc")
        # normaler rechtsklick
    if leftclick and end - start < delta:
        write_Shortcut("lc")
        # normaler linksklick
    touchcounter -= 1
    if touchcounter == 0:
        leftclick = True
    double = time.time()
    hold = False
    if False:  # GPIO.input(40):
        if super(Screen, self).on_touch_down(touch):
            return True
        if not self.collide_point(*touch.pos):
            return False
    write_release()
    # sichergehen, dass alle Tasten losgelassen werden


def calculate_dx_dy(inx, iny):
    global dx, dy, released, nmpx, nmpy, ompx, ompy
    dx, dy = 0, 0
    if released:
        ompx, ompy = inx, iny
        released = False
    else:
        nmpx, nmpy = inx, iny
        dx = nmpx - ompx
        dy = nmpy - ompy
        ompx = nmpx
        ompy = nmpy
    dx = int(dx)
    dy = int(dy)
