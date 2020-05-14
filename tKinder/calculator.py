from tkinter import *


class Calculator(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)


root = Tk()
root.geometry("400x300")
app = Calculator(root)
root.mainloop()
