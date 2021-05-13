from lib.hisat2_docker import hisat2
from lib.stringtie_docker import stringtie
from lib.deseq2_docker import deseq2
from lib.fastx_toolkit_docker import fastx_toolkit

def printing_return(fun,input_command):
        #input_command = input('Enter the Container Command: ')
        #self.log.write('\nContainer command used: {}'.format(self.input_command))

        if fun == 'hisat2':
            output = hisat2(input_command)
            if output:
                return "Hisat2 container successfully executed "
            else:
                return "error occured"
        
        if fun == 'stringtie':
            output = stringtie(input_command)
            if output == True:
                return "Stringtie container successfully executed "
            else:
                return "error occured"

        if fun == 'deseq2':
            output = deseq2(input_command)
            if output == True:
                return "deseq2 container successfully executed "
            else:
                return "error occured"

        if fun == 'fastx_toolkit':
            output = fastx_toolkit(input_command)
            if output == True:
                return "fastx_toolkit container successfully executed "
            else:
                return "error occured"