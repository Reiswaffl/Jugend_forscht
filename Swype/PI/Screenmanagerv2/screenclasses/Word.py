# coding=utf-8
from Screenmanagerv2.ScreenHandler import gethome
from Screenmanagerv2.TouchHandler import *


class Word(Screen):
    def send(self, value):
        write_write(value)
        print("sent " + str(value))

    def getHome(self):
        return gethome()

    def on_touch_down(self, touch):
        on_touch_down(self, touch, Screen)

    def on_touch_move(self, touch):
        on_touch_move(self, touch, Screen)

    def on_touch_up(self, touch):
        on_touch_up(self, touch, Screen)

    def pressed(self, button):
        print(button)
