# coding=utf-8
import RPi.GPIO as GPIO
import serial
import os

os.environ['KIVY_GL_BACKEND'] = 'gl'
import time
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.properties import ObjectProperty

# Touchpad wird initialisiert
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '600')
print("Touchpad setup done")

# GPIO setup; Widerstand wird initialisierd, Input festgelegt
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
print("GPIO setup done")

shortcutTime = time.time()
time.sleep(1)
# USBController wird initialisiert
# ser = serial.Serial(
#    port='/dev/ttyAMA0',
#    baudrate=115200,
#    parity=serial.PARITY_NONE,
#    stopbits=serial.STOPBITS_ONE,
#    bytesize=serial.EIGHTBITS,
#    timeout=1
# )
print("Serial initialisation done")


def write_Shortcut(shortcut):
    global shortcutTime
    if time.time() > shortcutTime + 0.5:
        print(shortcut)
        if not shortcut == "c3":
            shortcutTime = time.time()
    # ser.write(bin('SH' + shortcutNumber + '\n'))


def write_Movement(x, y):
    global shortcutTime
    if time.time() - 0.1 > shortcutTime:
        print(x, y)
    # ser.write(bin(x + ',' + y + '\n'))


def write_release():
    print("release all")
    # ser.write(bin('SH' + shortcutNumber + '\n'))


# Variablen werden initialisiert
touch = False
lasttime = 0
previousValue = 0
currentValue = 0
operator = "+"
touchcounter = 0
print("variables initialisation done")


class MainScreen(Screen):
    dx = 0
    dy = 0
    ompx = 0
    ompy = 0
    nmpx = 0
    nmpy = 0
    global touchcounter
    touchcounter = 0
    start = time.time()
    leftclick = False
    released = True
    end = time.time()
    double = time.time()
    delta = 0.1
    delta2 = 0.2
    hold = False

    def on_touch_down(self, touch):
        global touchcounter
        touchcounter += 1
        self.start = time.time()
        if self.start - self.double < self.delta2:
            self.hold = True
        if GPIO.input(40):
            if super(MainScreen, self).on_touch_down(touch):
                return True
            if not self.collide_point(*touch.pos):
                return False

    def on_touch_move(self, touch):
        self.end = time.time()
        if GPIO.input(40) == False and self.end - self.start > self.delta2:
            touch_input = touch.pos
            self.calculate_dx_dy(touch_input[0], touch_input[1])
            if self.hold:
                # linksklick gedrückt halten
                self.send("c3")
                self.send(0)
            else:
                self.send(0)  # Mausbewegung abgreifen
        elif GPIO.input(40):
            if super(MainScreen, self).on_touch_down(touch):
                return True
            if not self.collide_point(*touch.pos):
                return False

    def on_touch_up(self, touch):
        global touchcounter
        self.end = time.time()
        if touchcounter > 1:
            self.leftclick = False
        if self.end - self.start < self.delta and touchcounter == 2:
            self.send("c2")
        # normaler rechtsklick
        if self.leftclick and self.end - self.start < self.delta:
            self.send("c1")
        # normaler linksklick
        touchcounter -= 1
        if touchcounter == 0:
            self.leftclick = True
        self.double = time.time()
        self.hold = False
        if GPIO.input(40):  # GPIO.input(input_pin):  # buttonsDown:
            if super(MainScreen, self).on_touch_down(touch):
                return True
            if not self.collide_point(*touch.pos):
                return False
        write_release()
        # sichergehen, dass alle Tasten losgelassen werden
        pass

    def send(self, value):
        global touchcounter
        if value == 0:
            write_Movement(self.dx, self.dy)
        # Curserbewegung weitergeben
        else:
            write_Shortcut(value)
        # self.switch(code)
        # writeNumber(100)

    # print("x: "+str(self.dx)+"  y: "+str(self.dy)+" tc: "+str(touchcounter))
    # print(self.dy)

    def calculate_dx_dy(self, inx, iny):
        self.dx, self.dy = 0, 0
        if self.released:
            self.ompx, self.ompy = inx, iny
            self.released = False
        else:
            self.nmpx, self.nmpy = inx, iny
            self.dx = self.nmpx - self.ompx
            self.dy = self.nmpy - self.ompy

            self.ompx = self.nmpx
            self.ompy = self.nmpy

        self.dx = int(self.dx)
        self.dy = int(self.dy)


class Numpad(Screen):
    def send(self, value):
        write_Shortcut(value)
        print("sent " + str(value))


class Calculator(Screen):
    text = ObjectProperty("0")

    def send(self, value):
        write_Shortcut(value)

    def changeoperator(self, noperator):
        global operator
        global currentValue
        global previousValue
        if previousValue == 0:
            previousValue = currentValue
        else:
            self.totalup(currentValue)
        operator = noperator
        currentValue = 0

    def giveresult(self):
        global currentValue
        global previousValue
        self.totalup(currentValue)
        previousValue = 0
        currentValue = 0

    def reset(self):
        global previousValue
        global currentValue
        currentValue = 0
        previousValue = 0
        self.text = str(0)

    def calculate(self, value):
        global operator
        global currentValue
        currentValue *= 10
        currentValue += value
        self.text = str(currentValue)

    def totalup(self, value2):
        global operator
        global previousValue
        if operator == "+":
            previousValue += value2
            self.text = str(previousValue)
        elif operator == "-":
            previousValue -= value2
            self.text = str(previousValue)
        elif operator == "*":
            previousValue *= value2
            self.text = str(previousValue)
        elif operator == "/":
            if value2 != 0:
                previousValue /= value2
                self.text = str(previousValue)
            else:
                self.text = "Error"


class ScreenManagement(ScreenManager):
    def reset(self):
        global touchcounter
        touchcounter = 0


presentation = Builder.load_file("kivyfile.kv")


class MainApp(App):
    def build(self):
        return presentation


if __name__ == "__main__":
    MainApp().run()
