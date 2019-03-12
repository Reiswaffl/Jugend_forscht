# coding=utf-8
#import RPi.GPIO as GPIO
#import serial
import os

#os.environ['KIVY_GL_BACKEND'] = 'gl'
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


home = "main"


def switch():
    global home
    if home == 'main':
        home = 'testscreen2'
        return home
    elif home == 'testscreen2':
        home = 'testscreen3'
        return home
    elif home == 'testscreen3':
        home = 'main'
        return home
    else:
        home = 'main'
        return home


def sethome(nHome):
    global home
    home = nHome


def gethome():
    #global home
    return home

# ___________ Screen - Classes ____________


class MainScreen(Screen):
    def getHome(self):
        return gethome()

    def setHome(self, nHome):
        sethome(nHome)

    def Switch(self):
        return switch()


class TestScreen2(Screen):
    def Switch(self):
        return switch()


class TestScreen3(Screen):
    def Switch(self):
        return switch()


class Numpad(Screen):
    def send(self, value):
        write_Shortcut(value)
        print("sent " + str(value))

    def getHome(self):
        return gethome()


class Calculator(Screen):
    text = ObjectProperty("0")

    def getHome(self):
        return gethome()

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
