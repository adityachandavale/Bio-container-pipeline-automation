import os
import os.path
import time

from lib.printing_return import printing_return

    
def manual_mode(function_input,input_command):
    out = printing_return(function_input,input_command)
    if out:
        return 1
    else:
        return 0