import os
import os.path
import time

from lib.hisat2_docker import hisat2
from lib.stringtie_docker import stringtie
from lib.deseq2_docker import deseq2
from lib.fastx_toolkit_docker import fastx_toolkit

class Exec:

    input_command = None
    
    # Declaring counters for execution tracking
    cnt = 0
    cnt_bioconda = 0
    cnt_hisat2 = 0
    cnt_stringtie = 0
    cnt_deseq2 = 0
    cnt_fastx = 0
    
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
    #log.write("\nOutput folder name: {}".format(f_name))
    os.chdir(f_name) # Change program execution folder to newly created folder


    def __init__(self,function_input,input_command):
        #while(1):

            #function_input = input('Enter the Name of the Container to execute: ')
            #self.log.write("\nName of container executed: {}".format(function_input))

        self.input_command = input_command
        out = self.printing_return(function_input)

    def printing_return(self,fun):
        #self.input_command = input('Enter the Container Command: ')
        #self.log.write('\nContainer command used: {}'.format(self.input_command))

        if fun == 'hisat2':
            output = hisat2(self.input_command)
            if output == True:
                return "Hisat2 container successfully executed "
            else
                return "error occured"
        
        if fun == 'stringtie':
            output = stringtie(self.input_command)
            if output == True:
                return "Stringtie container successfully executed "
            else
                return "error occured"

        if fun == 'deseq2':
            output = deseq2(self.input_command)
            if output == True:
                return "deseq2 container successfully executed "
            else
                return "error occured"

        if fun == 'fastx_toolkit':
            output = fastx_toolkit(self.input_command)
            if output == True:
                return "fastx_toolkit container successfully executed "
            else
                return "error occured"

