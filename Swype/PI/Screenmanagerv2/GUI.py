# coding=utf-8
#import RPi.GPIO as GPIO
#import serial
import os

#os.environ['KIVY_GL_BACKEND'] = 'gl'
#import time
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.properties import ObjectProperty

# Touchpad wird initialisiert
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '600')
print("Touchpad setup done")

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
