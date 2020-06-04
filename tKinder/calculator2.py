from tkinter import *


class Calculator(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)


root = Tk()
app = Calculator(root)
root.mainloop()
