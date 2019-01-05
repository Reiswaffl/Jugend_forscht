import Tkinter as tkr
import logic

class userInterface(tkr.Tk):
    def __init__(self):
        tkr.Tk.__init__(self)
        self.SHORTCUTS = [
            "Shortcut1",
            "Shortcut2",
            "Shortcut3",
            "Shortcut4"
        ]
        self.var = tkr.StringVar()
        self.var.set(self.SHORTCUTS[0])
        self.var2 = tkr.StringVar()
        self.var2.set(self.SHORTCUTS[1])

    def select(self):
        print("selected " + self.var.get() + " for Shortcut 1")
        print("selected " + self.var2.get() + " for Shortcut 2")
        logic.writeShortcut('01','hotkey',self.var.get())
        logic.writeShortcut('02', 'hotkey', self.var2.get())

    def buildInterface(self):
        self.geometry("1500x1000")
        self.title("Swypad Window")

        tkr.Label(self, text="Shortcutoptions", font=("Arial", 18)).grid(row=0)

        tkr.Label(self, text="Shortcut 1", font=("Arial", 16)).grid(row=1, column=0)

        shortcutset = tkr.OptionMenu(self, self.var, *self.SHORTCUTS)
        shortcutset.configure(font=("Arial", 16))
        shortcutset.grid(row=1, column=1)

        tkr.Label(self, text="Shortcut 2", font=("Arial", 16)).grid(row=2, column=0)

        shortcutset2 = tkr.OptionMenu(self, self.var2, *self.SHORTCUTS)
        shortcutset2.configure(font=("Arial", 16))
        shortcutset2.grid(row=2, column=1)

        selectbutton = tkr.Button(master=self, text="Select", command=self.select, font=("Arial", 16))
        selectbutton.grid(row=3, column=0)
