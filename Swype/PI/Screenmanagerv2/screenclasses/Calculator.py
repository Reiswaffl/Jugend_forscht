from kivy.properties import ObjectProperty
from Screenmanagerv2.ScreenHandler import gethome
from Screenmanagerv2.TouchHandler import *

previousValue = 0
currentValue = 0
operator = "+"


class Calculator(Screen):
    text = ObjectProperty("0")

    def getHome(self):
        return gethome()

    def send(self, value):
        write_Shortcut(value)

    def changeoperator(self, noperator):
        global operator
        global currentValue
        global previousValue
        if previousValue == 0:
            previousValue = currentValue
        else:
            self.totalup(currentValue)
        operator = noperator
        currentValue = 0

    def giveresult(self):
        global currentValue
        global previousValue
        self.totalup(currentValue)
        previousValue = 0
        currentValue = 0

    def reset(self):
        global previousValue
        global currentValue
        currentValue = 0
        previousValue = 0
        self.text = str(0)

    def calculate(self, value):
        global operator
        global currentValue
        currentValue *= 10
        currentValue += value
        self.text = str(currentValue)

    def totalup(self, value2):
        global operator
        global previousValue
        if operator == "+":
            previousValue += value2
            self.text = str(previousValue)
        elif operator == "-":
            previousValue -= value2
            self.text = str(previousValue)
        elif operator == "*":
            previousValue *= value2
            self.text = str(previousValue)
        elif operator == "/":
            if value2 != 0:
                previousValue /= value2
                self.text = str(previousValue)
            else:
                self.text = "Error"

    def on_touch_down(self, touch):
        on_touch_down(self, touch, Screen)

    def on_touch_move(self, touch):
        on_touch_move(self, touch, Screen)

    def on_touch_up(self, touch):
        on_touch_up(self, touch, Screen)
