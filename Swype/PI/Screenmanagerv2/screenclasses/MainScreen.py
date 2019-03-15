# coding=utf-8
from Screenmanagerv2.ScreenHandler import gethome, sethome, switch
from Screenmanagerv2.TouchHandler import *


class MainScreen(Screen):
    @staticmethod
    def getHome():
        return gethome()

    @staticmethod
    def setHome(nHome):
        sethome(nHome)

    @staticmethod
    def Switch():
        return switch()

    def writeshortcut(self, Shortcut):
        write_Shortcut(Shortcut)

    def on_touch_down(self, touch):
        on_touch_down(self, touch, Screen)

    def on_touch_move(self, touch):
        on_touch_move(Screen, touch, Screen)

    def on_touch_up(self, touch):
        on_touch_up(Screen, touch, Screen)
