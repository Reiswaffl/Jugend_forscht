# coding=utf-8
from ScreenHandler import gethome
from TouchHandler import *


class Numpad(Screen):
    def send(self, value):
        write_write(value)

    def getHome(self):
        return gethome()

    def on_touch_down(self, touch):
        on_touch_down(self, touch, Screen)

    def on_touch_move(self, touch):
        on_touch_move(self, touch, Screen)

    def on_touch_up(self, touch):
        on_touch_up(self, touch, Screen)

    def sendSH(self, value):
        write_Shortcut(value)
