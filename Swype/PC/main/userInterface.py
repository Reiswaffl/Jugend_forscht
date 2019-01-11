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
        self.sh = tkr.StringVar()
        self.sh.set(self.SHORTCUTS[0])
        self.sh2 = tkr.StringVar()
        self.sh2.set(self.SHORTCUTS[1])
        self.sh3 = tkr.StringVar()
        self.sh3.set(self.SHORTCUTS[2])
        self.sh4 = tkr.StringVar()
        self.sh4.set(self.SHORTCUTS[3])

        self.cmd = tkr.StringVar()
        self.cmd.set(self.COMMAND[0])
        self.cmd2 = tkr.StringVar()
        self.cmd2.set(self.COMMAND[0])
        self.cmd3 = tkr.StringVar()
        self.cmd3.set(self.COMMAND[0])
        self.cmd4 = tkr.StringVar()
        self.cmd4.set(self.COMMAND[0])

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
        self.geometry("600x400")
        self.title("Swypad Window")

        tkr.Label(self, text="Shortcutoptions", font=("Arial", 18)).grid(row=0)

        self.buildShortcuts()
        self.buildCommands()

        selectbutton = tkr.Button(master=self, text="Select", command=self.select, font=("Arial", 16))
        selectbutton.grid(row=5, column=0)

    def buildShortcuts(self):
        tkr.Label(self, text="Shortcut 1", font=("Arial", 16)).grid(row=1, column=0)

        shortcutset = tkr.OptionMenu(self, self.sh, *self.SHORTCUTS)
        shortcutset.configure(font=("Arial", 16))
        shortcutset.grid(row=1, column=2)

        tkr.Label(self, text="Shortcut 2", font=("Arial", 16)).grid(row=2, column=0)

        shortcutset2 = tkr.OptionMenu(self, self.sh2, *self.SHORTCUTS)
        shortcutset2.configure(font=("Arial", 16))
        shortcutset2.grid(row=2, column=2)

        tkr.Label(self, text="Shortcut 3", font=("Arial", 16)).grid(row=3, column=0)

        shortcutset3 = tkr.OptionMenu(self, self.sh3, *self.SHORTCUTS)
        shortcutset3.configure(font=("Arial", 16))
        shortcutset3.grid(row=3, column=2)

        tkr.Label(self, text="Shortcut 4", font=("Arial", 16)).grid(row=4, column=0)

        shortcutset4 = tkr.OptionMenu(self, self.sh4, *self.SHORTCUTS)
        shortcutset4.configure(font=("Arial", 16))
        shortcutset4.grid(row=4, column=2)

    def buildCommands(self):
        cmdset = tkr.OptionMenu(self,self.cmd,*self.COMMAND)
        cmdset.configure(font=("Arial", 16))
        cmdset.grid(row=1,column=1)

        cmdset2 = tkr.OptionMenu(self,self.cmd2,*self.COMMAND)
        cmdset2.configure(font=("Arial", 16))
        cmdset2.grid(row=2,column=1)

        cmdset3 = tkr.OptionMenu(self,self.cmd3,*self.COMMAND)
        cmdset3.configure(font=("Arial", 16))
        cmdset3.grid(row=3,column=1)

        cmdset4 = tkr.OptionMenu(self,self.cmd4,*self.COMMAND)
        cmdset4.configure(font=("Arial", 16))
        cmdset4.grid(row=4,column=1)
