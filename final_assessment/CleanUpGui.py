from tkinter import *
from os import remove, listdir
from os.path import exists, getsize, isdir, isfile, join
import os

from tkinter import filedialog

from FileDetails import FileDetails
from FolderDetails import FolderDetails


class CleanUpGui(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master=master)
        self.master.title("Clean up")
        self.pack(fill=BOTH, expand=1)
        never_delete_files = open("never_delete_files.txt", "a+")

        # Setup variables
        self.folder_details = None
        self.current_file = None

        # Setup GUI elements
        self.current_file_name = Label(self)
        self.current_file_size = Label(self)
        self.type_file_info = Label(self)

        self.delete_file_button = Button(self, text="delete", command=self.delete_current_file)
        self.skip_file_button = Button(self, text="skip", command=self.load_next_file)
        self.never_delete_button = Button(self, text="never delete this file", command=self.never_delete)

        # Place GUI elements on Canvas
        self.current_file_name.pack()
        self.current_file_size.pack()
        self.type_file_info.pack()

        self.delete_file_button.pack()
        self.skip_file_button.pack()
        self.never_delete_button.pack()

    # process buttons

    def delete_current_file(self):
        # check if a current file is available
        ndfile = open("never_delete_files.txt", "r")
        ndfiles = ndfile.read().splitlines()
        path = join(self.folder_details.path, self.current_file.path)
        if path in ndfiles:
            print("in list, can't be deleted")  # show on GUI           #todo
            self.load_next_file()
        else:
            if self.current_file:
                print("will be deleted")  # show on GUI                 #todo
                remove(join(self.folder_details.path, self.current_file.path))
                # load the next file
                self.load_next_file()

    def load_next_file(self):
        if self.folder_details:
            next_file = self.folder_details.get_next_file()
            # ^^^ is the name of the file without extention
            if next_file:
                self.current_file = FileDetails(self, self.folder_details, next_file)
            else:
                self.current_file = FileDetails(self, self.folder_details, "")
            self.current_file.display_details()

    def never_delete(self):
        path = join(self.folder_details.path, self.current_file.path)
        file = open("never_delete_files.txt", "a")
        file.write(path + "\n")
        self.load_next_file()

    # startup

    def select_folder(self):
        folder_path = filedialog.askdirectory()
        self.folder_details = FolderDetails(folder_path)
        self.load_next_file()
