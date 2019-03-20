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
from screenclasses.Numpad import *
from screenclasses.MainScreen import *
from screenclasses.MainScreen2 import *
from screenclasses.Calculator import *
from screenclasses.Spotify import *
from screenclasses.Word import *
from SensorThread import *


# Touchpad wird initialisiert
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '600')
print("Touchpad setup done")

touchcounter = 0


class ScreenManagement(ScreenManager):
    pass


presentation = Builder.load_file("kivyfile.kv")

sensorThread.start()


class MainApp(App):
    def build(self):
        return presentation


if __name__ == "__main__":
    MainApp().run()
