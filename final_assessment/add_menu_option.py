# https://stackoverflow.com/questions/11295917/how-to-select-a-directory-and-store-the-location-using-tkinter-in-python


from tkinter import filedialog
from tkinter import *

root = Tk()
root.withdraw()
folder_selected = filedialog.askdirectory()
