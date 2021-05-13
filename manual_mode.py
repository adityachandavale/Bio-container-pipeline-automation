import os
import os.path
import time

from lib.printing_return import printing_return

class Exec:

    input_command = None

    def __init__(self,function_input,input_command):
        self.input_command = input_command
        #function_input = input('Enter the Name of the Container to execute: ')
        #self.input_command = input('Enter the Container Command: ')
        out = printing_return(function_input,self.input_command)

        print("Execution successful. Thank you for using.")