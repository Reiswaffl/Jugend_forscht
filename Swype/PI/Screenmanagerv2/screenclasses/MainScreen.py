from kivy.uix.screenmanager import Screen
from Screenmanagerv2.ScreenHandler import gethome, sethome, switch


class MainScreen(Screen):
    def getHome(self):
        return gethome()

    def setHome(self, nHome):
        sethome(nHome)

    def Switch(self):
        return switch()
