from tkinter import *


class Calculator(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)

        self.entrythingy = Entry()
        self.entrythingy.pack()
        self.contents = StringVar()
        # self.contents.set("this is a variable")
        self.entrythingy["textvariable"] = self.contents
        self.entrythingy.bind('<Key-Return>', self.function)

    def function(self, event):
        x = self.contents.get()
        print(x)


root = Tk()
root.geometry("400x300")
app = Calculator(root)
root.mainloop()
