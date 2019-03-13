from kivy.uix.screenmanager import Screen
from Screenmanagerv2.ScreenHandler import switch
from Screenmanagerv2.writerScript import *


class TestScreen2(Screen):
    def Switch(self):
        return switch()

    def writeshortcut(self, shortcut):
        write_Shortcut(shortcut)
