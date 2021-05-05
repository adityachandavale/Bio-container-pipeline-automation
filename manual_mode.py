import os
import os.path
import time

#from lib.hisat2_docker import hisat2
#from lib.stringtie_docker import stringtie
#from lib.deseq2_docker import deseq2
#from lib.bioconda_py import bioconda
#from lib.fastx_toolkit_docker import fastx_toolkit

class Exec:
    # Appending to log file for execution status.
    #log = open("logs/manual_mode_execution.txt","a")
    #log.write("\nExecution start time: [ {} ]".format(str(time.time())))

    # Declaring Input command to be used for the respectively invoked Container
    input_command = None
    
    # Declaring counters for execution tracking
    cnt = 0
    cnt_bioconda = 0
    cnt_hisat2 = 0
    cnt_stringtie = 0
    cnt_deseq2 = 0
    cnt_fastx = 0
    
    # Changing path to Output directory
    #path = os.path.abspath(os.path.join(os.getcwd(),'outputs'))
    #os.chdir(path)
    
    # Reading counter number previously appended to file
    f = open("counter.txt","r")
    a = f.read()
    b = int(a)+1

    # Writing a new number to be appended to current file.
    f1 = open("counter.txt","w")
    f1.write(str(b))
    f1.close()

    f_name = "output_genome" + str(b) # new appended folder name
    #os.mkdir(f_name) # create folder
    #log.write("\nOutput folder name: {}".format(f_name))
    #os.chdir(f_name) # Change program execution folder to newly created folder


    def __init__(self,input_command):
        #while(1):

            #function_input = input('Enter the Name of the Container to execute: ')
            #self.log.write("\nName of container executed: {}".format(function_input))

            #if function_input == 'hisat2' or function_input == 'stringtie' or function_input == 'deseq2' or function_input == 'bioconda' or function_input == 'fastx_toolkit':
            self.input_command = input_command
            #out = self.printing_return(function_input)
            #self.cnt += 1
            #return out
            #else:
                #print("Wrong container name\n enter again ")
                #self.log.write("\nError: Wrong container name specified.")
                
            #input_choice = input('Do you want to execute another container?\n y / n\n')
            #if input_choice == 'n' or input_choice == 'N':                    
                #self.log.write('\nBioconda executed {} times'.format(self.cnt_bioconda))
                #self.log.write('\nhisat2 executed {} times'.format(self.cnt_hisat2))
                #self.log.write('\nstringtie executed {} times'.format(self.cnt_stringtie))
                #self.log.write('\ndeseq2 executed {} times'.format(self.cnt_deseq2))
                #self.log.write('\nfastx_toolkit executed {} times'.format(self.cnt_fastx))
            #    break
                    
        #self.log.write("\nTotal executions {}".format(self.cnt))             
        #self.log.write("\n\nExecution end time: [ {} ]".format(str(time.time())))

    def printing_return(self,fun):
        #self.input_command = input('Enter the Container Command: ')
        #self.log.write('\nContainer command used: {}'.format(self.input_command))

        if fun == 'hisat2':
            #output_hisat = hisat2(self.input_command)
            #output_hisat = print(self.input_command)
            self.cnt_hisat2 += 1
            #print(output_hisat)
            return "Hisat2 container successfully executed "
        if fun == 'stringtie':
            #output_stringtie = stringtie(self.input_command)
            #output_stringtie = print(self.input_command)
            self.cnt_stringtie += 1
            #print(output_stringtie)
            return "Stringtie container successfully executed "
        if fun == 'deseq2':
            #output_deseq2 = deseq2(self.input_command)
            #output_deseq2 = print(self.input_command)
            self.cnt_deseq2 += 1
            #print(output_deseq2)
            return "Deseq2 container successfully executed "
        if fun == 'fastx_toolkit':
            #output_fastx = fastx_toolkit(self.input_command)
            #output_fastx = print(self.input_command)
            self.cnt_fastx += 1
            #print(output_fastx)
            return "fastx container successfully executed "

