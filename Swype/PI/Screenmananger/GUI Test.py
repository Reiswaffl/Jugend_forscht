from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.properties import ObjectProperty
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '600')

touch = False
lasttime = 0
previousValue = 0
currentValue = 0
operator = "+"


class MainScreen(Screen):
    def send(self, code):
        print(self.switch(code))

    def switch(self,argument):
        switcher = {
            1: "Strg + c",
            2: "Strg + v",
            3: "Null"
        }
        return switcher.get(argument, "Fail")

class Calculator(Screen):
    text = ObjectProperty("0")

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


class Numpad(Screen):
    pass


class ScreenManagement(ScreenManager):
    pass


presentation = Builder.load_file("main Test.kv")


class MainApp(App):

    def build(self):
        return presentation


if __name__ == "__main__":
    MainApp().run()
