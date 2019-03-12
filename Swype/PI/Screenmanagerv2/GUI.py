# coding=utf-8
#import RPi.GPIO as GPIO
#import serial
import os

os.environ['KIVY_GL_BACKEND'] = 'gl'
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


class MainScreen(Screen):
    pass


class TestScreen2(Screen):
    pass


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
