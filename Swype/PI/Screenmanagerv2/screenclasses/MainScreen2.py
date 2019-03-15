from Screenmanagerv2.ScreenHandler import switch
from Screenmanagerv2.TouchHandler import *


class TestScreen2(Screen):
    def Switch(self):
        return switch()

    def on_touch_down(self, touch):
        on_touch_down(self, touch, Screen)

    def on_touch_move(self, touch):
        on_touch_move(self, touch, Screen)

    def on_touch_up(self, touch):
        on_touch_up(self, touch, Screen)

    def writeshortcut(self, Shortcut):
        write_Shortcut(Shortcut)
