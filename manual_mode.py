import os
import os.path

from lib.hisat2_docker import hisat2
from lib.stringtie_docker import stringtie
from lib.deseq2_docker import deseq2
from lib.bioconda_py import bioconda
from lib.fastx_toolkit_docker import fastx_toolkit

class Exec:
    input_command = None
    cnt = 0
    cnt_bioconda = 0
    cnt_hisat2 = 0
    cnt_stringtie = 0
    cnt_deseq2 = 0
    cnt_fastx = 0
    
    path = os.path.abspath(os.path.join(os.getcwd(),'outputs'))
    os.chdir(path)
    f = open("counter.txt","r")
    a = f.read()
    b = int(a)+1

    f1 = open("counter.txt","w")
    f1.write(str(b))
    f1.close()

    f_name = "output_genome" + str(b)
    #current_name = "outputs"
    os.mkdir(f_name)
    os.chdir(f_name)


    def __init__(self):
        while(1):

            if self.cnt == 0:
                function_input = input('Enter the Container to execute: ')
                if function_input == 'hisat2' or function_input == 'stringtie' or function_input == 'deseq2' or function_input == 'bioconda' or function_input == 'fastx_toolkit':
                    self.printing_return(function_input)
                    self.cnt += 1
                else:
                    print("Wrong container name\n enter again ")
            else:
                input_choice = input('Do you want to execute another container?\n y / n\n')
                if input_choice == 'y' or input_choice == 'Y':
                    function_input = input('Enter the Container to execute: ')
                    self.printing_return(function_input)
                    self.cnt += 1
                else:
                    print('Bioconda executed {} times'.format(self.cnt_bioconda))
                    print('hisat2 executed {} times'.format(self.cnt_hisat2))
                    print('stringtie executed {} times'.format(self.cnt_stringtie))
                    print('deseq2 executed {} times'.format(self.cnt_deseq2))
                    print('fastx_toolkit executed {} times'.format(self.cnt_fastx))

                    break
                    
        print("Total executions",self.cnt)               

    def printing_return(self,fun):
        self.input_command = input('Enter the Container Command: ')
        if fun == 'hisat2':
            output_hisat = hisat2(self.input_command)
            self.cnt_hisat2 += 1
            print(output_hisat)
        if fun == 'stringtie':
            output_stringtie = stringtie(self.input_command)
            self.cnt_stringtie += 1
            print(output_stringtie)
        if fun == 'deseq2':
            output_deseq2 = deseq2(self.input_command)
            self.cnt_deseq2 += 1
            print(output_deseq2)
        if fun == 'fastx_toolkit':
            output_fastx = fastx_toolkit(self.input_command)
            self.cnt_fastx += 1
            print(output_fastx)
        if fun == 'bioconda':
            output_bioconda = bioconda(self.input_command)
            self.cnt_bioconda += 1
            print(output_bioconda)

class Test:
    a = Exec()
