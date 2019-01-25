# coding=utf-8
import time
import os
os.environ['KIVY_GL_BACKEND'] = 'gl'
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.properties import ObjectProperty

Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '600')

touch = False
lasttime = 0
previousValue = 0
currentValue = 0
operator = "+"


def writeNumber(value):
    # bus.write_byte(address,value)
    print(value)
    return -1


class MainScreen(Screen):
    dx = 0
    dy = 0
    package = 0
    ompx = 0
    ompy = 0
    nmpx = 0
    nmpy = 0
    touchcounter = 0
    start = time.time()
    leftclick = True
    released = True
    end = time.time()
    double = time.time()
    delta = 0.08
    delta2 = 0.2
    hold = False
"gedrückt"

    def on_touch_down(self, touch):
        self.touchcounter += 1
        self.start = time.time()
        if self.start - self.double < self.delta2:
            self.hold = True

        if False:  # GPIO.input(input_pin):  # buttonsDown:
            if super(MainScreen, self).on_touch_down(touch):
                return True
            if not self.collide_point(*touch.pos):
                return False

    def on_touch_move(self, touch):
        self.end = time.time()
        if False == False and self.end - self.start > self.delta2:  # erstes False muss durch GPIO.input(input_pin)
            # ersetzt werden
            touch_input = touch.pos
            # no 3D-touch
            self.calculate_dx_dy(touch_input[0], touch_input[1])
            self.calculate_package()
            if self.hold:
                self.send(5)
            else:
                self.send(0)

    def on_touch_up(self, touch):
        self.end = time.time()
        if self.touchcounter > 1:
            self.leftclick = False
        if self.end - self.start < self.delta and self.touchcounter == 2:
            self.send(4)
        if self.leftclick and self.end - self.start < self.delta:
            self.send(3)
        self.touchcounter -= 1
        if self.touchcounter == 0:
            self.leftclick = True
        self.double = time.time()
        self.hold = False
        self.send(6)

    def send(self, code):
        self.switch(code)
        writeNumber(self.package)

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

    def calculate_package(self):
        # calculate number for x from movement
        if self.dx == 0:
            mx = 0
        elif self.dx < 0:
            if (self.dx * -1) < 7:
                mx = 6
            elif (self.dx * -1) < 14:
                mx = 7
            elif (self.dx * -1) < 21:
                mx = 8
            else:
                mx = 9
        else:
            if self.dx < 7:
                mx = 1
            elif self.dx < 14:
                mx = 2
            elif self.dx < 21:
                mx = 3
            else:
                mx = 4
        # calculate number for y from movement
        if self.dy == 0:
            my = 0
        elif self.dy < 0:
            if (self.dy * -1) < 7:
                my = 6
            elif (self.dy * -1) < 14:
                my = 7
            elif (self.dy * -1) < 21:
                my = 8
            else:
                my = 9
        else:
            if self.dy < 7:
                my = 1
            elif self.dy < 14:
                my = 2
            elif self.dy < 21:
                my = 3
            else:
                my = 4
        # calculate whole number and
        # save the glorious number that is going to be the package that is send to the receiver
        self.package = mx * 10 + my


class Calculator(Screen):
    text = ObjectProperty("0")

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
    pass


presentation = Builder.load_file("main.kv")


class MainApp(App):

    def build(self):
        return presentation


if __name__ == "__main__":
    MainApp().run()
