# coding=utf-8
# import RPi.GPIO as GPIO
# import serial
import os
# Import Kivy Stuff
# os.environ['KIVY_GL_BACKEND'] = 'gl'
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.config import Config

# Import Screens for Kivy
from Screenmanagerv2.screenclasses.Numpad import *
from Screenmanagerv2.screenclasses.MainScreen import *
from Screenmanagerv2.screenclasses.MainScreen2 import *
from Screenmanagerv2.screenclasses.Calculator import *
from Screenmanagerv2.screenclasses.Spotify import *
from Screenmanagerv2.screenclasses.Word import *


# Touchpad wird initialisiert
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '600')
print("Touchpad setup done")

touchcounter = 0


class ScreenManagement(ScreenManager):
    pass


presentation = Builder.load_file("kivyfile.kv")


class MainApp(App):
    def build(self):
        return presentation


if __name__ == "__main__":
    MainApp().run()
