import docker
import os

class Exec:
    client = docker.from_env()
    input_command = None
    cnt = 0
    count = 1

    os.chdir("/home/aditya/Documents/MSC-DS/Sem3/Bio-container-pipeline-automation/outputs")
    f_name = "output" + str(count)
    current_name = "/home/aditya/Documents/MSC-DS/Sem3/Bio-container-pipeline-automation/outputs"
    count += 1
    os.mkdir(os.path.join(current_name,f_name))

    def __init__(self):
        while(1):
            if self.cnt == 0:
                function_input = input('Enter the Container to execute:')
                if function_input == 'hisat2' or function_input == 'stringtie' or function_input == 'deseq2' or function_input == 'bioconda':
                    self.printing_return(function_input)
                    self.cnt += 1
                else:
                    print("Wrong container name\n enter again")
            else:
                input_choice = input('Do you want to execute another container?\n y / n\n')
                if input_choice == 'y' or input_choice == 'Y':
                    function_input = input('Enter the Container to execute:')
                    self.printing_return(function_input)
                    self.cnt += 1
                else:
                    print("bye")
                    break
                    

        print("Total executions",self.cnt)
                
    def bioconda(self):
        a = os.system(self.input_command)
        return a

    def hisat2(self):
        a = self.client.containers.run('336d8edb337f',self.input_command)
        return a

    def stringtie(self):
        b = self.client.containers.run('3aec4555231e',self.input_command)
        return b

    def deseq2(self):
        c = self.client.containers.run('8d620dc67af7',self.input_command)
        return c

    def printing_return(self,fun):
        self.input_command = input('Enter the Container Command')
        if fun == 'hisat2':
            output_hisat = self.hisat2()
            print(output_hisat)
        if fun == 'stringtie':
            output_stringtie = self.stringtie()
            print(output_stringtie)
        if fun == 'deseq2':
            output_deseq2 = self.deseq2()
            print(output_deseq2)
        if fun == 'bioconda':
            output_bioconda = self.bioconda()
            print(output_bioconda)

class Test:
    a = Exec()
