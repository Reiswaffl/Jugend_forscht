from kivy.uix.screenmanager import Screen
from Screenmanagerv2.writerScript import write_Shortcut
from Screenmanagerv2.ScreenHandler import gethome


class Numpad(Screen):
    def send(self, value):
        write_Shortcut(value)
        print("sent " + str(value))

    def getHome(self):
        return gethome()
