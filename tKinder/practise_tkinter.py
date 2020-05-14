from tkinter import *
from PIL import Image, ImageTk


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)

        # quitButton = Button(self, text="Quit", command=self.client_exit)
        # quitButton.place(x=200, y=200)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        # add file button
        file = Menu(menu)
        file.add_command(label="Save")
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)

        # add edit button
        edit = Menu(menu)
        edit.add_command(label="Show Image", command=self.showImg)
        edit.add_command(label="Show text", command=self.showTxt)
        menu.add_cascade(label="Edit", menu=edit)

    def showImg(self):
        load = Image.open("foto.jpg")
        render = ImageTk.PhotoImage(load)

        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

    def showTxt(self):
        text = Label(self, text="hello hellooooo")
        text.pack()

    def client_exit(self):
        exit()


root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()
