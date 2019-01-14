import Tkinter as tkr
import logic

class userInterface(tkr.Tk):
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
        logic.writeShortcut('01',self.cmd[0].get(),  self.sh[0].get())
        logic.writeShortcut('02',self.cmd[1].get(), self.sh[1].get())
        logic.writeShortcut('03',self.cmd[2].get(), self.sh[2].get())
        logic.writeShortcut('04',self.cmd[3].get(), self.sh[3].get())
        logic.writeShortcut('05',self.cmd[4].get(),  self.sh[4].get())
        logic.writeShortcut('06',self.cmd[5].get(), self.sh[5].get())
        logic.writeShortcut('07',self.cmd[6].get(), self.sh[6].get())
        logic.writeShortcut('08',self.cmd[7].get(), self.sh[7].get())

    def buildInterface(self):
        self.geometry("1500x600")
        self.title("Swypad Window")
        self.buildCommandsStack(0,1,1)
        self.buildShortcutsStack(0,1,2)
        self.buildCommandsStack(4,1,4)
        self.buildShortcutsStack(4,1,5)
        self.buildLabels()

        selectbutton = tkr.Button(master=self, text="Select", command=self.select, font=("Arial", 16))
        selectbutton.grid(row=5, column=0)

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

    def buildLabels(self):
        tkr.Label(self, text="Shortcutoptions", font=("Arial", 18)).grid(row=0)

        tkr.Label(self, text="Shortcut 1", font=("Arial", 16)).grid(row=1, column=0)
        tkr.Label(self, text="Shortcut 2", font=("Arial", 16)).grid(row=2, column=0)
        tkr.Label(self, text="Shortcut 3", font=("Arial", 16)).grid(row=3, column=0)
        tkr.Label(self, text="Shortcut 4", font=("Arial", 16)).grid(row=4, column=0)
        tkr.Label(self, text="Shortcut 5", font=("Arial", 16)).grid(row=1, column=3)
        tkr.Label(self, text="Shortcut 6", font=("Arial", 16)).grid(row=2, column=3)
        tkr.Label(self, text="Shortcut 7", font=("Arial", 16)).grid(row=3, column=3)
        tkr.Label(self, text="Shortcut 8", font=("Arial", 16)).grid(row=4, column=3)
    def load(self):
        for i in range(8):
            self.sh[i].set(logic.)