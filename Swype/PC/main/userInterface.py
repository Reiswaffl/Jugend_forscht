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
            tkr.StringVar()
        ]
        self.cmd = [
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

        self.cmd[0].set(self.COMMAND[0])
        self.cmd[1].set(self.COMMAND[0])
        self.cmd[2].set(self.COMMAND[0])
        self.cmd[3].set(self.COMMAND[0])

    def select(self):
        print("selected " + self.sh.get() + " for Shortcut 1")
        print("selected " + self.sh2.get() + " for Shortcut 2")
        print("selected " + self.sh3.get() + " for Shortcut 3")
        print("selected " + self.sh4.get() + " for Shortcut 4")
        logic.writeShortcut('01','hotkey',self.sh.get())
        logic.writeShortcut('02', 'hotkey', self.sh2.get())
        logic.writeShortcut('03', 'hotkey', self.sh3.get())
        logic.writeShortcut('04', 'hotkey', self.sh4.get())

    def buildInterface(self):
        self.geometry("900x600")
        self.title("Swypad Window")

        self.buildShortcutsStack(0,1,2)
        self.buildShortcutsStack(4,1,5)
        self.buildCommandsStack(0,1,2)
        self.buildLabels()

        selectbutton = tkr.Button(master=self, text="Select", command=self.select, font=("Arial", 16))
        selectbutton.grid(row=5, column=0)

    def buildShortcutsStack(self,index, rowOffset, columnOffset):
        for i in range(4):
            self.shortcut[i+index] = tkr.OptionMenu(self,self.sh[i%4],*self.SHORTCUTS)
            self.shortcut[i+index].configure(font=("Arial", 16))
            self.shortcut[i+index].grid(row=(rowOffset+i%4),column=columnOffset)



    def buildCommandsStack(self,index,rowOffset,columnOffset):
        for i in range(4):
            self.command[i+index] = tkr.OptionMenu(self,self.cmd[i],*self.COMMAND)
            self.command[i+index].configure(font=("Arial",16))
            self.command[i+index].grid(row=(rowOffset+i),column=columnOffset)

    def buildLabels(self):
        tkr.Label(self, text="Shortcutoptions", font=("Arial", 18)).grid(row=0)

        tkr.Label(self, text="Shortcut 1", font=("Arial", 16)).grid(row=1, column=0)

        tkr.Label(self, text="Shortcut 2", font=("Arial", 16)).grid(row=2, column=0)

        tkr.Label(self, text="Shortcut 3", font=("Arial", 16)).grid(row=3, column=0)

        tkr.Label(self, text="Shortcut 4", font=("Arial", 16)).grid(row=4, column=0)