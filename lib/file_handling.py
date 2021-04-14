import os
import os.path

def file_handling():
    log = open("logs/manual_mode_execution.txt","a")
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
    return f_name