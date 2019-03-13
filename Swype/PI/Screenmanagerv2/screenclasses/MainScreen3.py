from kivy.uix.screenmanager import Screen
from Screenmanagerv2.ScreenHandler import switch


class TestScreen3(Screen):
    def Switch(self):
        return switch()
