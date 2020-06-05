from os.path import exists, join, getsize
from tkinter import *
from PIL import ImageTk, Image


class FileDetails():
    def __init__(self, cleanUpGui, folder, path):
        self.gui = cleanUpGui
        self.folder = folder
        self.path = path  # name file without extention

    def display_details(self):
        if self.path != "" and exists(join(self.folder.path, self.path)):
            self.gui.current_file_name.configure(text="file name: " + self.path)
            file_size = getsize(join(self.folder.path, self.path))
            self.gui.current_file_size.configure(text="file size: " + str(file_size))

            filepath = join(self.folder.path, self.path)
            # test if file is text file
            if filepath.endswith(".txt") == True:
                fline = open(filepath, "r").readline()
                self.gui.type_file_info.configure(
                    text="file type is .txt\n\n Here is a preview of content:\n" + '"' + fline + '"')
            else:
                # test if file is an image
                list = [".jpg", ".png", ".gif", ".tif"]
                for ext in list:
                    if filepath.endswith(ext) == True:
                        self.gui.type_file_info.configure(text="file is an image")
                        im = Image.open(filepath)  # not a preview in tkinter       #todo
                        im.show()
                        break
                else:
                    self.gui.type_file_info.configure(text="")
        else:
            self.gui.current_file_name.configure(text="file name: <no file selected>")
            self.gui.current_file_size.configure(text="file size: <no file selected>")
            self.gui.type_file_info.configure(text="")
