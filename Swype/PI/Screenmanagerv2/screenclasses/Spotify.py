from kivy.uix.screenmanager import Screen
from Screenmanagerv2.ScreenHandler import gethome
from Screenmanagerv2.writerScript import *

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
