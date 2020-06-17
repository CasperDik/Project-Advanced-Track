from os.path import exists, join, getsize
from tkinter import *
from PIL import ImageTk, Image


class FileDetails():
    def __init__(self, cleanUpGui, folder, path):
        self.gui = cleanUpGui
        self.folder = folder
        self.path = path  # name file without extention

    def display_details(self):  # dispaly filename, filesize, preview text/image etc
        if self.path != "" and exists(join(self.folder.path, self.path)):
            self.gui.current_file_name.configure(text="file name: " + self.path)
            file_size = getsize(join(self.folder.path, self.path))
            self.gui.current_file_size.configure(text="file size: " + str(file_size))
            self.gui.never_delete_this_file.configure(text="")

            filepath = join(self.folder.path, self.path)
            # check if file is text file + show preview of first line file
            if filepath.endswith(".txt") == True:
                fline = open(filepath, "r").readline()
                self.gui.type_file_info.configure(
                    text="file type is: .txt\n\n Here is a preview of content:\n\n" + '"' + fline + '"'"\n")
            else:
                # test if file is an image + load image in new canvas
                list = [".jpg", ".png", ".gif", ".tif"]
                for ext in list:
                    if filepath.endswith(ext) == True:
                        self.gui.type_file_info.configure(text="file is an image\n")

                        root = Toplevel()
                        self.img = ImageTk.PhotoImage(Image.open(filepath))
                        canvas = Canvas(root, width=self.img.width() * 1.2, height=self.img.height() * 1.2)
                        root.title("Preview")
                        canvas.pack(fill=BOTH, expand=1)
                        canvas.create_image(20, 20, anchor=NW, image=self.img)

                        break
                else:
                    self.gui.type_file_info.configure(text="")
        else:
            self.gui.current_file_name.configure(text="file name: <no file selected>")
            self.gui.current_file_size.configure(text="file size: <no file selected>")
            self.gui.type_file_info.configure(text="")
            self.gui.disable_buttons()
