import os
import os.path
import time

from lib.printing_return import printing_return

class Exec:

    input_command = None

    # Changing path to Output directory
    path = os.path.abspath(os.path.join(os.getcwd(),'outputs'))
    os.chdir(path)
    
    # Reading counter number previously appended to file
    f = open("counter.txt","r")
    a = f.read()
    b = int(a)+1

    # Writing a new number to be appended to current file.
    f1 = open("counter.txt","w")
    f1.write(str(b))
    f1.close()

    f_name = "output_genome" + str(b) # new appended folder name
    os.mkdir(f_name) # create folder
    os.chdir(f_name) # Change program execution folder to newly created folder


    def __init__(self,function_input,input_command):
        self.input_command = input_command
        #function_input = input('Enter the Name of the Container to execute: ')
        #self.input_command = input('Enter the Container Command: ')
        out = printing_return(function_input,self.input_command)

        print("Execution successful. Thank you for using.")