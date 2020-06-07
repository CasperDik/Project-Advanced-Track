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

        # checkbox
        self.checkvar1 = IntVar()

        # bytes deleted counter
        self.bytes_counter = 0

        # Setup GUI elements
        self.current_file_name = Label(self)
        self.current_file_size = Label(self)
        self.type_file_info = Label(self)
        self.never_delete_this_file = Label(self)

        self.bytes_counter_label = Label(self)

        self.delete_file_button = Button(self, text="delete", command=self.delete_current_file)
        self.skip_file_button = Button(self, text="skip", command=self.load_next_file)
        self.never_delete_button = Checkbutton(self, text="never delete this file", variable=self.checkvar1, onvalue=1,
                                               offvalue=0, command=self.combined_function)
        self.bytes_counter_label.configure(text="current bytes deleted: " + str(self.bytes_counter))

        # Place GUI elements on Canvas
        self.current_file_name.pack()
        self.current_file_size.pack()
        self.never_delete_this_file.pack()
        self.type_file_info.pack()
        self.bytes_counter_label.pack()
        self.delete_file_button.pack()
        self.skip_file_button.pack()
        self.never_delete_button.pack()

    # process buttons
    def combined_function(self):
        self.prevent_unchecking()
        self.never_delete()

    def delete_current_file(self):
        # check if a current file is available
        ndfile = open("never_delete_files.txt", "r")
        ndfiles = ndfile.read().splitlines()
        path = join(self.folder_details.path, self.current_file.path)
        if path in ndfiles:
            self.never_delete_this_file.configure(text="The file" + self.current_file.path + " cannot be deleted")
        else:
            if self.current_file:
                file_size = getsize(join(self.folder_details.path, self.current_file.path))
                self.bytes_counter += file_size
                self.bytes_counter_label.configure(text="current bytes deleted: " + str(self.bytes_counter))
                remove(join(self.folder_details.path, self.current_file.path))
                # load the next file
                self.load_next_file()

    def load_next_file(self):
        if self.folder_details:
            next_file = self.folder_details.get_next_file()
            # ^^^ is the name of the file without extention
            if next_file:
                self.current_file = FileDetails(self, self.folder_details, next_file)
                self.check_not_delete_list()
                self.prevent_unchecking()
            else:
                self.current_file = FileDetails(self, self.folder_details, "")
                self.check_not_delete_list()
                self.prevent_unchecking()
            self.current_file.display_details()

    def never_delete(self):
        path = join(self.folder_details.path, self.current_file.path)
        file = open("never_delete_files.txt", "a")
        file.write(path + "\n")

    def check_not_delete_list(self):
        ndfile = open("never_delete_files.txt", "r")
        ndfiles = ndfile.read().splitlines()
        path = join(self.folder_details.path, self.current_file.path)
        if path in ndfiles:
            self.checkvar1.set(1)
        else:
            self.checkvar1.set(0)

    def prevent_unchecking(self):
        if self.checkvar1.get() == 1:
            self.never_delete_button.config(state=DISABLED)
        else:
            self.never_delete_button.config(state=NORMAL)

    # startup
    def select_folder(self):
        folder_path = filedialog.askdirectory()
        self.folder_details = FolderDetails(folder_path)
        self.load_next_file()
        self.check_not_delete_list()
        self.prevent_unchecking()
