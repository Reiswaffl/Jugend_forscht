# coding=utf-8
import Tkinter as tkr
import subprocess
from logic import *

global p


class DisplayingClass(tkr.Tk):
    def __init__(self):
        tkr.Tk.__init__(self)
        self.logic = Logic()
        self.r = dataWriterReader.Reader()
        self.shortcuts = self.r.getShortcuts()
        self.spotifyShortcuts = self.r.getSpotifyShortcuts()
        self.running = False
        self.p = None

        self.title("Swypad Window")

        # crazy Shit für eine sehr sehr einfache Oberfläche
        self.shortcut = []
        tkr.Label(self, text="Shortcutoptions", font=("Arial", 18)).grid(row=0)
        tkr.Label(self, text="COM: ", font=("Arial", 16)).grid(row=0, column=3)
        self.comBox = tkr.Entry()
        self.comBox.grid(row=0, column=4)
        self.comBox.insert(0, self.logic.getCOM())

        self.z = 25
        self.z2 = 0
        self.z3 = 0
        try:
            for i in range(self.z):
                tkr.Label(self, text=self.shortcuts[i].get('command'), font=("Arial", 16)).grid(row=i+1, column=0)
                self.z2 += 1
        except:
            pass

        try:
            for i in range(self.z):
                tkr.Label(self, text=self.spotifyShortcuts[i].get('command'), font=("Arial", 16)).grid(row=i+1, column=3)
                self.z3 += 1
        except:
            pass
        for i in range(self.z2):
            self.shortcut.append(tkr.Entry())
            self.shortcut[i + 0].grid(row=(1 + (i % self.z2)), column=2)
            self.shortcut[i + 0].insert(0, str(self.shortcuts[i].text))
        for i in range(self.z3):
            self.shortcut.append(tkr.Entry())
            self.shortcut[i + self.z2].grid(row=(1 + (i % self.z2)), column=4)
            self.shortcut[i + self.z2].insert(0, str(self.spotifyShortcuts[i].text))

        self.selectbutton = tkr.Button(master=self, text="Save Config", command=self.select, font=("Arial", 14))
        self.selectbutton.grid(row=self.z2+1, column=4)
        self.startButton = tkr.Button(master=self, text="start Connection", command=self.start, font=("Arial", 14))
        self.startButton.grid(row=self.z2+1, column=3)

    def select(self):
        try:
            for i in range(self.z2):
                self.r.setShortcut(str(i), self.shortcut[i].get())
        except:
            pass
        try:
            for i in range(self.z3):
                self.r.setSpotifyShortcut(str(i), self.shortcut[i + self.z2].get())
        except:
            pass

        self.r.setCOM(self.comBox.get())

    def start(self):
        if not self.running:
            print('started')
            self.running = True
            self.startButton.config(text='stop Connection')
            self.r.setCOM(self.comBox.get())
            self.p = subprocess.Popen(['python', 'serialHandling.py', 'arg1', 'arg2'])
        else:
            self.running = False
            self.startButton.config(text='start Connection')
            self.p.terminate()


class UserInterface(tkr.Tk):
    serialRunning = False

    def __init__(self):
        self.logic = Logic()
        tkr.Tk.__init__(self)
        self.COMMAND = [
            "hotkey",
            "scroll",
            "program"
        ]
        self.cmd = [
            tkr.StringVar(),
            tkr.StringVar(),
            tkr.StringVar(),
            tkr.StringVar(),
            tkr.StringVar(),
            tkr.StringVar(),
            tkr.StringVar(),
            tkr.StringVar()
        ]
        self.shortcut = [
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None
        ]
        self.command = [
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None
        ]
        self.cmd[0].set(self.COMMAND[0])
        self.cmd[1].set(self.COMMAND[0])
        self.cmd[2].set(self.COMMAND[0])
        self.cmd[3].set(self.COMMAND[0])
        self.cmd[4].set(self.COMMAND[0])
        self.cmd[5].set(self.COMMAND[0])
        self.cmd[6].set(self.COMMAND[0])
        self.cmd[7].set(self.COMMAND[0])

    def select(self):
        for i in range(8):
            if self.cmd[i].get() == "scroll":
                self.logic.writeShortcut(str(i), self.cmd[i].get(), "i" + self.shortcut[i].get())
            else:
                self.logic.writeShortcut(str(i), self.cmd[i].get(), self.shortcut[i].get())

    def start(self):
        if not self.serialRunning:
            print(self.comBox.get())
            global p
            self.logic.setCOM(self.comBox.get())
            p = subprocess.Popen(['python', 'serialHandling.py', 'arg1', 'arg2'])
            self.startButton.config(text="stop Connection")
            self.serialRunning = True
        else:
            p.terminate()
            self.startButton.config(text="start Connection")
            self.serialRunning = False

    def buildInterface(self):
        self.geometry("1560x600")
        self.title("Swypad Window")
        self.loadInformation()
        self.buildCommandsStack(0, 1, 1)
        self.buildShortcutsStack(0, 1, 2)
        self.buildCommandsStack(4, 1, 4)
        self.buildShortcutsStack(4, 1, 5)
        self.buildRest()
        self.buildLabels()

    def buildShortcutsStack(self, index, rowOffset, columnOffset):
        for i in range(4):
            self.shortcut[i + index] = tkr.Entry()
            self.shortcut[i + index].grid(row=(rowOffset + (i % 4)), column=columnOffset)
            #c, s = self.logic.getShortCut(str(i + index))
            #self.shortcut[i + index].insert(c, s)
            # self.shortcut[i+index] = tkr.OptionMenu(self,self.sh[i+index],*self.SHORTCUTS)
            # self.shortcut[i+index].configure(font=("Arial", 16))
            # self.shortcut[i+index].grid(row=(rowOffset+(i%4)),column=columnOffset)

    def buildCommandsStack(self, index, rowOffset, columnOffset):
        for i in range(4):
            self.command[i + index] = tkr.OptionMenu(self, self.cmd[i + index], *self.COMMAND)
            self.command[i + index].configure(font=("Arial", 16))
            self.command[i + index].grid(row=(rowOffset + (i % 4)), column=columnOffset)

    def buildRest(self):
        self.selectbutton = tkr.Button(master=self, text="Select", command=self.select, font=("Arial", 16))
        self.selectbutton.grid(row=5, column=0)

        self.comBox = tkr.Entry()
        self.comBox.grid(row=0, column=2)
        self.comBox.insert(0, self.logic.getCOM())

        self.startButton = tkr.Button(master=self, text="start Connection", command=self.start, font=("Arial", 14))
        self.startButton.grid(row=0, column=3)

    def buildLabels(self):
        tkr.Label(self, text="Shortcutoptions", font=("Arial", 18)).grid(row=0)
        tkr.Label(self, text="COM: ", font=("Arial", 16)).grid(row=0, column=1)
        tkr.Label(self, text="Shortcut 1", font=("Arial", 16)).grid(row=1, column=0)
        tkr.Label(self, text="Shortcut 2", font=("Arial", 16)).grid(row=2, column=0)
        tkr.Label(self, text="Shortcut 3", font=("Arial", 16)).grid(row=3, column=0)
        tkr.Label(self, text="Shortcut 4", font=("Arial", 16)).grid(row=4, column=0)
        tkr.Label(self, text="Shortcut 5", font=("Arial", 16)).grid(row=1, column=3)
        tkr.Label(self, text="Shortcut 6", font=("Arial", 16)).grid(row=2, column=3)
        tkr.Label(self, text="Shortcut 7", font=("Arial", 16)).grid(row=3, column=3)

    def loadInformation(self):
        for i in range(8):
            c, s = self.logic.getShortCut(str(i))
            self.cmd[i].set(c)

    def updateGUI(self):
        pass


'''interface = UserInterface()
interface.buildInterface()
interface.mainloop()
try:
    global p
    p.terminate()
except:
    pass'''
