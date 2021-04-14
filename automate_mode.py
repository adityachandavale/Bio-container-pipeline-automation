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

class auto_exec:
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

    multithread_cnt = 0

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
    def __init__(self):
        self.printing_return('hisat2')
        self.event_handling()
        self.write_log()

    # ----------------------------------------------------------------------------------------------------------------------

    # Running the containers
    def printing_return(self, fun):
        self.input_command = input('Enter the Container Command: ')
        self.log.write('\nContainer command used: {}'.format(self.input_command))

        if fun == 'hisat2':
            output_hisat = hisat2(self.input_command)
            self.log.write("hisat2 command used: {}".format(self.input_command))
            self.cnt_hisat2 += 1
            print(output_hisat)
        if fun == 'stringtie':
            output_stringtie = stringtie(self.input_command)
            self.log.write("stringtie command used: {}".format(self.input_command))
            self.cnt_stringtie += 1
            print(output_stringtie)
        if fun == 'deseq2':
            output_deseq2 = deseq2(self.input_command)
            self.log.write("deseq2 command used: {}".format(self.input_command))
            self.cnt_deseq2 += 1
            print(output_deseq2)
        if fun == 'fastx_toolkit':
            output_fastx = fastx_toolkit(self.input_command)
            self.log.write("fast_toolkit command used: {}".format(self.input_command))
            self.cnt_fastx += 1
            print(output_fastx)
        if fun == 'bioconda':
            output_bioconda = bioconda(self.input_command)
            self.log.write("bioconda command used: {}".format(self.input_command))
            self.cnt_bioconda += 1
            print(output_bioconda)

    # ---------------------------------------------------------------------------------------------------------------------------s

    # Event handler and automation of pipeline
    def event_handling(self):
        patterns = "*"
        ignore_patterns = ""
        ignore_directories = False
        case_sensitive = False
        automation_event_handler = PatternMatchingEventHandler(patterns,ignore_patterns,ignore_directories,case_sensitive)

        def on_created(event):
            #print(f"Event, {event.src_path} has been created")
            if event.src_path.endswith('.ht2'):
                self.printing_return('hisat2')
            if event.src_path.endswith('.sam') or event.src_path.endswith('.bam'):
                self.printing_return('stringtie')
            if event.src_path.endswith('.gtf'):
                self.printing_return('deseq2')
            if event.src_path.endswith('.csv'):
                print("Pipeline generated csv succesfully")
                self.multithread_cnt = 1


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
                if self.multithread_cnt == 0:
                    time.sleep(1)
                else:
                    self.write_log()
                    exit()

        except KeyboardInterrupt:
            automation_observer.stop()
            automation_observer.join()

    # --------------------------------------------------------------------------------------------------------------------------

    # Writing logs
    def write_log(self):
        self.log.write('\nBioconda executed {} times'.format(self.cnt_bioconda))
        self.log.write('\nhisat2 executed {} times'.format(self.cnt_hisat2))
        self.log.write('\nstringtie executed {} times'.format(self.cnt_stringtie))
        self.log.write('\ndeseq2 executed {} times'.format(self.cnt_deseq2))
        self.log.write('\nfastx_toolkit executed {} times'.format(self.cnt_fastx)) 

class test:
    a = auto_exec()