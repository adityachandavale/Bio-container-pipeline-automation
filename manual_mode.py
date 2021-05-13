import os
import os.path
import time
import tkinter as tk
from tkinter import filedialog

from lib.printing_return import printing_return

root = tk.Tk()
root.withdraw()
root.lift()
root.focus_force()

class Exec:

    input_command = None

    # Changing path to Output directory
    print('Select an output folder')
    path = filedialog.askdirectory()
    os.chdir(path)
    print('Path of folder selected:\n',path,'\n')



    def __init__(self,function_input,input_command):
        self.input_command = input_command
        #function_input = input('Enter the Name of the Container to execute: ')
        #self.input_command = input('Enter the Container Command: ')
        out = printing_return(function_input,self.input_command)

        print("Execution successful. Thank you for using.")