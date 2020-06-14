from tkinter import *
from os import remove, listdir
from os.path import exists, getsize, isdir, isfile, join
import os
import shutil

from tkinter import filedialog
from tkinter.ttk import Progressbar

from FileDetails import FileDetails
from FolderDetails import FolderDetails


# todo: error handling --> rename: weird filenames/not allowed symbols, delete: already deleted manuallt after start running program,

class CleanUpGui(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master=master)
        self.master.title("Clean up")

        self.grid(row=12, column=3, sticky=NSEW)
        self.progress = Progressbar(self, orient=HORIZONTAL, length=200, maximum=100, mode='determinate')

        file = open("never_delete_files.txt", "w+")

        # Setup variables
        self.folder_details = None
        self.current_file = None
        self.new_path = ""

        # dummy, =1 if in never_delete_files.txt, otherwise =0
        self.checkvar1 = IntVar()

        # bytes deleted counter
        self.bytes_counter = 0

        # Setup GUI elements
        self.current_file_name = Label(self)
        self.current_file_size = Label(self)
        self.type_file_info = Label(self)
        self.never_delete_this_file = Label(self)
        self.bytes_counter_label = Label(self)
        self.rename_button = Label(self)

        # buttons
        self.delete_file_button = Button(self, text="delete", command=self.delete_current_file)
        self.skip_file_button = Button(self, text="skip", command=self.load_next_file)
        self.never_delete_button = Checkbutton(self, text="never delete this file", variable=self.checkvar1, onvalue=1,
                                               offvalue=0, command=self.combined_function1)
        self.bytes_counter_label.configure(text="current bytes deleted: " + str(self.bytes_counter))
        self.rename_button = Button(self, text="rename file", command=self.rename_window)
        self.quick_move_button = Button(self, text="Quick Move", command=self.quick_move)

        # Place GUI elements on Canvas
        self.progress.grid(row=0, column=0, columnspan=3)
        self.current_file_name.grid(row=1, column=0, columnspan=3, rowspan=1, sticky="W")
        self.current_file_size.grid(row=2, column=0, columnspan=3, rowspan=1, sticky="W")
        self.bytes_counter_label.grid(row=3, column=0, columnspan=3, rowspan=1, sticky="W")

        self.never_delete_this_file.grid(row=4, column=0, columnspan=3, rowspan=1, sticky="NESW")
        self.type_file_info.grid(row=5, column=0, columnspan=3, rowspan=4, sticky="NESW")

        self.quick_move_button.grid(row=10, column=0, columnspan=3, rowspan=1, sticky="ESW")

        self.delete_file_button.grid(row=11, column=0, columnspan=1, rowspan=1, sticky="ESW")
        self.skip_file_button.grid(row=11, column=1, columnspan=1, rowspan=1, sticky="ESW")
        self.rename_button.grid(row=11, column=2, columnspan=1, rowspan=1, sticky="ESW")

        self.never_delete_button.grid(row=12, column=0, columnspan=3, rowspan=1, sticky="W")

    # steps of the progress bar for each file
    def progress_bar(self):
        n = self.folder_details.n_files
        steps = (100 - 0.001) / n
        self.progress.step(steps)

    # to execute 2 functions with 1 button press
    def combined_function1(self):
        self.prevent_unchecking()
        self.never_delete()

    # delete files with button press
    def delete_current_file(self):
        # check if file is not in the "never_delete_file" i.e. box is unchecked/dummy equal to 0
        if self.checkvar1.get() == 1:
            self.never_delete_this_file.configure(text="The file" + self.current_file.path + " cannot be deleted")
        else:  # if not in the .txt file then delete, load next file and count the bytes deleted
            if self.current_file:
                file_size = getsize(join(self.folder_details.path, self.current_file.path))
                self.bytes_counter += file_size
                self.bytes_counter_label.configure(text="current bytes deleted: " + str(self.bytes_counter))
                remove(join(self.folder_details.path, self.current_file.path))
                # load the next file
                self.load_next_file()

    # load next file
    def load_next_file(self):
        if self.folder_details:
            next_file = self.folder_details.get_next_file()
            if next_file:  # load next file, check if it can be deleted, disable/enable checkbox, move progress bar
                self.current_file = FileDetails(self, self.folder_details, next_file)
                self.check_not_delete_list()
                self.prevent_unchecking()
                self.progress_bar()
            else:
                self.current_file = FileDetails(self, self.folder_details, "")
                self.check_not_delete_list()
                self.prevent_unchecking()
            self.current_file.display_details()

    # write absolute path to txt file, to never deleted a file with that exact absolute path
    def never_delete(self):
        path = join(self.folder_details.path, self.current_file.path)
        file = open("never_delete_files.txt", "a")
        file.write(path + "\n")

    # check if file can be deleted, check the checkbox if not/uncheck if it can
    def check_not_delete_list(self):
        ndfile = open("never_delete_files.txt", "r")
        ndfiles = ndfile.read().splitlines()
        path = join(self.folder_details.path, self.current_file.path)
        if path in ndfiles:
            self.checkvar1.set(1)
        else:
            self.checkvar1.set(0)

    # check if file can be deleted, if not disable checkbox
    def prevent_unchecking(self):
        if self.checkvar1.get() == 1:
            self.never_delete_button.config(state=DISABLED)
        else:
            self.never_delete_button.config(state=NORMAL)

    # rename a file with user input + if file is in never_deleted_file add the new path to the text file
    def rename_file(self):
        path = join(self.folder_details.path, self.current_file.path)
        new_name = join(self.folder_details.path, self.entry.get())
        os.rename(path, new_name)

        if self.checkvar1.get() == 1:
            path = join(self.folder_details.path, self.entry.get())
            file = open("never_delete_files.txt", "a")
            file.write(path + "\n")

        self.root.destroy()
        self.load_next_file()

    # open new canvas, ask for user input to rename, execute function rename_file if button pressed
    def rename_window(self):
        self.root = Tk()
        self.root.title("Rename File")
        new_window = Canvas(self.root, width=200, height=100)

        self.entry = Entry(self.root)
        self.entry.insert(0, str(self.current_file.path))
        new_window.create_window(100, 35, window=self.entry)

        label = Label(self.root, text="Type your new file name here:\n\n Include the extension in the new file name!")
        b = Button(self.root, text="rename", width=10, command=self.rename_file)

        label.pack()
        new_window.pack()
        b.place(x=65, y=110)

    # disable buttons when went through all files, to prevent any errors from occurring
    def disable_buttons(self):
        self.delete_file_button["state"] = DISABLED
        self.rename_button["state"] = DISABLED
        self.never_delete_button["state"] = DISABLED
        self.skip_file_button["state"] = DISABLED
        self.quick_move_button["state"] = DISABLED

    # Move file to selected directory, raise error if no directory selected to move the file to
    def quick_move(self):
        try:
            if self.new_path == "":
                self.new_path = filedialog.askdirectory()
            shutil.move(join(self.folder_details.path, self.current_file.path), self.new_path)
            self.load_next_file()
        except FileNotFoundError:
            print("no directory selected to move the file to")
        # todo: safe file in configuration file?

    # startup
    # select directory and 'start' the program, raise error if no directory selected
    def select_folder(self):
        try:
            folder_path = filedialog.askdirectory()
            self.folder_details = FolderDetails(folder_path)
            self.load_next_file()
            self.check_not_delete_list()
            self.prevent_unchecking()
        except AttributeError:
            print("no folder selected")
            raise SystemExit
