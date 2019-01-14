import Tkinter as tkr
import logic
import subprocess

class userInterface(tkr.Tk):
    serialRunning = False
    def __init__(self):
        tkr.Tk.__init__(self)
        self.SHORTCUTS = [
            "ctrl+c",
            "ctrl+v",
            "alt+f4",
            "alt+tab"
        ]
        self.COMMAND = [
            "hotkey",
            "scroll"
        ]
        self.sh = [
            tkr.StringVar(),
            tkr.StringVar(),
            tkr.StringVar(),
            tkr.StringVar(),
            tkr.StringVar(),
            tkr.StringVar(),
            tkr.StringVar(),
            tkr.StringVar()
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
        self.sh[0].set(self.SHORTCUTS[0])
        self.sh[1].set(self.SHORTCUTS[1])
        self.sh[2].set(self.SHORTCUTS[2])
        self.sh[3].set(self.SHORTCUTS[3])
        self.sh[4].set(self.SHORTCUTS[0])
        self.sh[5].set(self.SHORTCUTS[1])
        self.sh[6].set(self.SHORTCUTS[2])
        self.sh[7].set(self.SHORTCUTS[3])
        self.cmd[0].set(self.COMMAND[0])
        self.cmd[1].set(self.COMMAND[0])
        self.cmd[2].set(self.COMMAND[0])
        self.cmd[3].set(self.COMMAND[0])
        self.cmd[4].set(self.COMMAND[0])
        self.cmd[5].set(self.COMMAND[0])
        self.cmd[6].set(self.COMMAND[0])
        self.cmd[7].set(self.COMMAND[0])
    def select(self):
        logic.writeShortcut('0',self.cmd[0].get(),  self.sh[0].get())
        logic.writeShortcut('1',self.cmd[1].get(), self.sh[1].get())
        logic.writeShortcut('2',self.cmd[2].get(), self.sh[2].get())
        logic.writeShortcut('3',self.cmd[3].get(), self.sh[3].get())
        logic.writeShortcut('4',self.cmd[4].get(),  self.sh[4].get())
        logic.writeShortcut('5',self.cmd[5].get(), self.sh[5].get())
        logic.writeShortcut('6',self.cmd[6].get(), self.sh[6].get())
        logic.writeShortcut('7',self.cmd[7].get(), self.sh[7].get())

    def start(self):
        if self.serialRunning == False:
            self.p = subprocess.Popen(['python', 'serialHandling.py', 'arg1', 'arg2'])
            self.startButton.config(text="stop Connection")
            self.serialRunning = True
        else:
            self.p.terminate()
            self.startButton.config(text="start Connection")
            self.serialRunning = False

    def buildInterface(self):
        self.geometry("1560x600")
        self.title("Swypad Window")
        self.loadInformation()
        self.buildCommandsStack(0,1,1)
        self.buildShortcutsStack(0,1,2)
        self.buildCommandsStack(4,1,4)
        self.buildShortcutsStack(4,1,5)
        self.buildRest()
        self.buildLabels()

    def buildShortcutsStack(self,index, rowOffset, columnOffset):
        for i in range(4):
            print(str(i+index) + "   " + str(columnOffset) + "   " + str(rowOffset+(i%4)))
            self.shortcut[i+index] = tkr.OptionMenu(self,self.sh[i+index],*self.SHORTCUTS)
            self.shortcut[i+index].configure(font=("Arial", 16))
            self.shortcut[i+index].grid(row=(rowOffset+(i%4)),column=columnOffset)


    def buildCommandsStack(self,index,rowOffset,columnOffset):
        for i in range(4):
            self.command[i+index] = tkr.OptionMenu(self,self.cmd[i+index],*self.COMMAND)
            self.command[i+index].configure(font=("Arial",16))
            self.command[i+index].grid(row=(rowOffset+(i%4)),column=columnOffset)

    def buildRest(self):
        self.selectbutton = tkr.Button(master=self, text="Select", command=self.select, font=("Arial", 16))
        self.selectbutton.grid(row=5, column=0)

        self.comBox = tkr.Entry()
        self.comBox.grid(row=0, column=2)
        self.comBox.insert(0,"COM1")

        self.startButton = tkr.Button(master=self,text="start Connection",command=self.start,font=("Arial",14))
        self.startButton.grid(row=0, column=3)

    def buildLabels(self):
        tkr.Label(self, text="Shortcutoptions", font=("Arial", 18)).grid(row=0)
        tkr.Label(self, text="COM: ",font=("Arial",16)).grid(row=0, column=1)
        tkr.Label(self, text="Shortcut 1", font=("Arial", 16)).grid(row=1, column=0)
        tkr.Label(self, text="Shortcut 2", font=("Arial", 16)).grid(row=2, column=0)
        tkr.Label(self, text="Shortcut 3", font=("Arial", 16)).grid(row=3, column=0)
        tkr.Label(self, text="Shortcut 4", font=("Arial", 16)).grid(row=4, column=0)
        tkr.Label(self, text="Shortcut 5", font=("Arial", 16)).grid(row=1, column=3)
        tkr.Label(self, text="Shortcut 6", font=("Arial", 16)).grid(row=2, column=3)
        tkr.Label(self, text="Shortcut 7", font=("Arial", 16)).grid(row=3, column=3)
        tkr.Label(self, text="Shortcut 8", font=("Arial", 16)).grid(row=4, column=3)
    def loadInformation(self):
        for i in range(8):
            c,s = logic.getShortCut(str(i))
            self.sh[i].set(s)
            self.cmd[i].set(c)


