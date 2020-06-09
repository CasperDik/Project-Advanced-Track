from tkinter import *
from os import remove, listdir
from os.path import exists, getsize, isdir, isfile, join
import os

from tkinter import filedialog

from FileDetails import FileDetails
from FolderDetails import FolderDetails


# todo: Allow the user to create ”quick move” folders where they can move the current file to that folder. (These should also be saved in a/the configuration file).
# todo: add progress bar?

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
        self.rename = Label(self)
        self.bytes_counter_label = Label(self)

        # buttons
        self.delete_file_button = Button(self, text="delete", command=self.delete_current_file)
        self.skip_file_button = Button(self, text="skip", command=self.load_next_file)
        self.never_delete_button = Checkbutton(self, text="never delete this file", variable=self.checkvar1, onvalue=1,
                                               offvalue=0, command=self.combined_function1)
        self.bytes_counter_label.configure(text="current bytes deleted: " + str(self.bytes_counter))
        self.rename = Button(text="rename file", command=self.rename_window)

        # Place GUI elements on Canvas
        self.current_file_name.pack()  # todo: create nice layout, improvement 1?
        self.current_file_size.pack()
        self.never_delete_this_file.pack()
        self.type_file_info.pack()
        self.bytes_counter_label.pack()
        self.delete_file_button.pack()
        self.skip_file_button.pack()
        self.rename.pack()
        self.never_delete_button.pack()

    # process buttons
    def combined_function1(self):  # to execute 2 functions with 1 button press
        self.prevent_unchecking()
        self.never_delete()

    def delete_current_file(self):
        #check if file is not in the "never_delete_file"
        ndfile = open("never_delete_files.txt", "r")
        ndfiles = ndfile.read().splitlines()
        path = join(self.folder_details.path, self.current_file.path)
        if path in ndfiles:
            self.never_delete_this_file.configure(text="The file" + self.current_file.path + " cannot be deleted")
        else:  # if not in the .txt file then deleted, load next file and count the bytes deleted
            if self.current_file:
                file_size = getsize(join(self.folder_details.path, self.current_file.path))
                self.bytes_counter += file_size
                self.bytes_counter_label.configure(text="current bytes deleted: " + str(self.bytes_counter))
                remove(join(self.folder_details.path, self.current_file.path))
                # load the next file
                self.load_next_file()

    def load_next_file(self):  # load next file
        if self.folder_details:
            next_file = self.folder_details.get_next_file()
            if next_file:  # load next file, check if it can be deleted, disable/enable checkbox
                self.current_file = FileDetails(self, self.folder_details, next_file)
                self.check_not_delete_list()
                self.prevent_unchecking()
            else:
                self.current_file = FileDetails(self, self.folder_details, "")
                self.check_not_delete_list()
                self.prevent_unchecking()
            self.current_file.display_details()

    def never_delete(self):  # write absolute path to txt file, to never deleted a file with that absolute path
        path = join(self.folder_details.path, self.current_file.path)
        file = open("never_delete_files.txt", "a")
        file.write(path + "\n")

    def check_not_delete_list(self):  # check if file can be deleted, check the checkbox if not/uncheck if it can
        ndfile = open("never_delete_files.txt", "r")
        ndfiles = ndfile.read().splitlines()
        path = join(self.folder_details.path, self.current_file.path)
        if path in ndfiles:
            self.checkvar1.set(1)
        else:
            self.checkvar1.set(0)

    def prevent_unchecking(self):  # check if file can be deleted, if not disable checkbox
        if self.checkvar1.get() == 1:
            self.never_delete_button.config(state=DISABLED)
        else:
            self.never_delete_button.config(state=NORMAL)

    def rename_file(
            self):  # rename a file with userinput + if file is in never_deleted_file add new path to the text file
        path = join(self.folder_details.path, self.current_file.path)
        new_name = join(self.folder_details.path, self.entry.get())  # todo: error handling --> if no extention
        os.rename(path, new_name)

        if self.checkvar1.get() == 1:
            path = join(self.folder_details.path, self.entry.get())
            file = open("never_delete_files.txt", "a")
            file.write(path + "\n")

        self.root.destroy()
        self.load_next_file()

    def rename_window(
            self):  # open new canvas, ask for user input to rename, execute function rename_file if button pressed
        self.root = Tk()
        self.root.title("Rename File")
        new_window = Canvas(self.root, width=200, height=100)

        self.entry = Entry(self.root)
        self.entry.insert(0, str(self.current_file.path))
        new_window.create_window(100, 35, window=self.entry)

        label = Label(self.root, text="Type your new file name here:\n\n Include the extention in the new file name!")
        b = Button(self.root, text="rename", width=10, command=self.rename_file)

        label.pack()
        new_window.pack()
        b.place(x=65, y=110)

    # startup
    def select_folder(self):  # select folder and 'start' program, raise error if no folder selected
        try:
            folder_path = filedialog.askdirectory()
            self.folder_details = FolderDetails(folder_path)
            self.load_next_file()
            self.check_not_delete_list()
            self.prevent_unchecking()
        except AttributeError:
            print("no folder selected")
            raise SystemExit
