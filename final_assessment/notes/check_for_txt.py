# https://stackoverflow.com/questions/5899497/how-can-i-check-the-extension-of-a-file
# https://stackoverflow.com/questions/51166970/how-can-i-check-if-only-txt-file-exists-in-a-directory-with-python

import os

file = "final_assessment/messy_folder/hoi"

if os.path.splitext(file)[1] == ".txt":
    print("yess!!")
