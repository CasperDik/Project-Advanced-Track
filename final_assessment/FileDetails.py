from os.path import exists, join, getsize
from tkinter import *
import os

class FileDetails():

    def __init__(self, cleanUpGui, folder, path):
        self.gui = cleanUpGui
        self.folder = folder
        self.path = path  # name file without extention

    def display_details(self):
        for file in os.listdir(self.folder.path):
            if file.endswith(".txt"):
                self.gui.type_file_info.configure(text="file type is .txt")

        if self.path != "" and exists(join(self.folder.path, self.path)):
            self.gui.current_file_name.configure(text="file name: " + self.path)
            file_size = getsize(join(self.folder.path, self.path))
            self.gui.current_file_size.configure(text="file size: " + str(file_size))
        else:
            self.gui.current_file_name.configure(text="file name: <no file selected>")
            self.gui.current_file_size.configure(text="file size: <no file selected>")
