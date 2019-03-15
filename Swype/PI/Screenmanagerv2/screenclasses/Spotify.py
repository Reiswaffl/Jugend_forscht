# coding=utf-8
from Screenmanagerv2.ScreenHandler import gethome
from Screenmanagerv2.TouchHandler import *

stepwidth = 0.1


class Spotify(Screen):
    def getHome(self):
        return gethome()

    def getStep(self):
        global stepwidth
        return stepwidth

    def getValue(self):
        return 0

    def getRange(self):
        return 0, 100

    def getVolume(self):
        return 10

    def getTitle(self):
        return 'Title by Interprete'

    def playPause(self):
        print('play/pause')

    def forward(self):
        print('forward')

    def back(self):
        print('back')

    def on_touch_down(self, touch):
        on_touch_down(self, touch, Screen)

    def on_touch_move(self, touch):
        on_touch_move(self, touch, Screen)

    def on_touch_up(self, touch):
        on_touch_up(self, touch, Screen)
