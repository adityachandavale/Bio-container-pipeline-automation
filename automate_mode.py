import time
import os
import os.path
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from lib.hisat2_docker import hisat2
from lib.stringtie_docker import stringtie
from lib.deseq2_docker import deseq2
from lib.bioconda_py import bioconda
from lib.fastx_toolkit_docker import fastx_toolkit

input_command = None

# Appending to log file for execution status.
log = open("logs/automatic_mode_execution.txt","a")
log.write("\nExecution start time: [ {} ]".format(str(time.time())))

# Declaring counters for execution tracking
cnt = 0
cnt_bioconda = 0
cnt_hisat2 = 0
cnt_stringtie = 0
cnt_deseq2 = 0
cnt_fastx = 0

# --------------------------------------------------------------------------------------------------------------------

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
log.write("\nOutput folder name: {}".format(f_name))
os.chdir(f_name) # Change program execution folder to newly created folder

# ----------------------------------------------------------------------------------------------------------------------

# Running the containers
def printing_return(fun):
    input_command = input('Enter the Container Command: ')
    log.write('\nContainer command used: {}'.format(input_command))

    if fun == 'hisat2':
        output_hisat = hisat2(input_command)
        cnt_hisat2 += 1
        print(output_hisat)
    if fun == 'stringtie':
        output_stringtie = stringtie(input_command)
        cnt_stringtie += 1
        print(output_stringtie)
    if fun == 'deseq2':
        output_deseq2 = deseq2(input_command)
        cnt_deseq2 += 1
        print(output_deseq2)
    if fun == 'fastx_toolkit':
        output_fastx = fastx_toolkit(input_command)
        cnt_fastx += 1
        print(output_fastx)
    if fun == 'bioconda':
        output_bioconda = bioconda(input_command)
        cnt_bioconda += 1
        print(output_bioconda)

# ---------------------------------------------------------------------------------------------------------------------------

printing_return(hisat2)

# ----------------------------------------------------------------------------------------------------------------------

# Event handler and automation of pipeline
patterns = "*"
ignore_patterns = ""
ignore_directories = False
case_sensitive = False
automation_event_handler = PatternMatchingEventHandler(patterns,ignore_patterns,ignore_directories,case_sensitive)

def on_created(event):
    #print(f"Event, {event.src_path} has been created")
    if event.src_path.endswith('.ht2'):
        printing_return(hisat2)
    if event.src_path.endswith('.sam') or event.src_path.endswith('.bam'):
        printing_return(stringtie)
    if event.src_path.endswith('.gtf'):
        printing_return(deseq2)
    if event.src_path.endswith('.csv'):
        print("Pipeline generated csv succesfully")
        automation_observer.stop()
        automation_observer.join()


def on_deleted(event):
    print(f"Event, {event.src_path} has been deleted")

automation_event_handler.on_created = on_created
automation_event_handler.on_deleted = on_deleted

path="."
go_recursively = True
automation_observer = Observer()
automation_observer.schedule(automation_event_handler, path, recursive=go_recursively)
automation_observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    automation_observer.stop()
    automation_observer.join()

# --------------------------------------------------------------------------------------------------------------------------

# Writing logs
log.write('\nBioconda executed {} times'.format(cnt_bioconda))
log.write('\nhisat2 executed {} times'.format(cnt_hisat2))
log.write('\nstringtie executed {} times'.format(cnt_stringtie))
log.write('\ndeseq2 executed {} times'.format(cnt_deseq2))
log.write('\nfastx_toolkit executed {} times'.format(cnt_fastx))