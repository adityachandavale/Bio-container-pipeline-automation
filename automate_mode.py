import time
import os
import os.path
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

from lib.printing_return import printing_return

class auto_exec:
    input_command = None

    multithread_cnt = 0


    # ----------------------------------------------------------------------------------------------------------------------
    def __init__(self,input_command):
    #def __init__(self):
        #self.input_command = input_command
        #function_input = input('Enter the Name of the Container to execute: ')
        
        printing_return('hisat2',self.input_command)
        self.event_handling()
        
    # ---------------------------------------------------------------------------------------------------------------------------s

    # Event handler and automation of pipeline
    def event_handling(self):
        patterns = "*"
        ignore_patterns = ""
        ignore_directories = False
        case_sensitive = False
        automation_event_handler = PatternMatchingEventHandler(patterns,ignore_patterns,ignore_directories,case_sensitive)

        def on_created(event):
            print(f"Event, {event.src_path} has been created")
            if event.src_path.endswith('.ht2'):
                printing_return('hisat2',self.input_command)
            if event.src_path.endswith('.sam') or event.src_path.endswith('.bam'):
                printing_return('stringtie',self.input_command)
            if event.src_path.endswith('.gtf'):
                printing_return('deseq2',self.input_command)
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
                    #self.write_log()
                    break
                    exit()

        except KeyboardInterrupt:
            automation_observer.stop()
            automation_observer.join()