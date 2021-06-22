#import automate_mode
from flask import Flask,render_template,request
from manual_mode import manual_mode as mm
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import os
import os.path
import time


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Choice',methods=['POST','GET'])
def myCheck():
    if(request.method=='POST'):
        a = request.form['rd1']
        print(a)
        if(a=='Manual'):
            return render_template('Manual.html')
        else:
            return render_template('Automation.html')

@app.route('/Manual',methods=['POST','GET'])
def manual():
    if(request.method=='POST'):
        a=request.form['containers']
        b=request.form['t1']

        e = mm(a,b)
        #c = e.printing_return(a)
    return ("<html><b>"+a+"</b></html> Container executed succesfully with query <html><b>"+b+"</b></html>")

def find_files(filename, search_path):
    result = []
    for root, dir, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(root, filename))
    print("Result in function ",result)
    return result


@app.route('/Automation',methods=['POST','GET'])
def auto():
    if(request.method=='POST'):
        
        i=0
        multithread_cnt = 0
        
        a = request.form['t1']
        b = request.form['t2']
        c = request.form['t3']
        d = request.form['t4']
        u1 = request.form['u1']
        fn = request.form['filename']
        #print("Usename ",type(u1))
        #print("Filename with path ",type(fn))
        result = find_files(fn,"/home/grp6")
        #print(result)
        #print("Result ",result)

        if((u1 in result)):
            r = mm('hisat2',a)
            print("hisat2 executed")
            if r == 1:
                r2 = mm('hisat2',b)
                print('Hisat2 executed successfully')
                if(r2 == 1):
                    r3 = mm('stringtie',c)
                    print('Stringtie executed successfully')
                    if(r3 == 1):
                        return "Thank You"
            '''else:
                print('Hisat2 not executed')
            
            def event_handling():
                patterns = "*"
                ignore_patterns = ""
                ignore_directories = False
                case_sensitive = False
                automation_event_handler = PatternMatchingEventHandler(patterns,ignore_patterns,ignore_directories,case_sensitive)
        
                def on_created(event):
                    if event.src_path.endswith('*.ht2'):
                        r = mm('hisat2',b)
                        if r == 1:
                            print('Hisat2 executed successfully')
                        else:
                            print('Hisat2 not executed')

                    if event.src_path.endswith('.sam') or event.src_path.endswith('.bam'):
                        r = mm('stringtie',c)
                        if r == 1:
                            print('Stringtie executed successfully')
                        else:
                            print('Stringtie not executed')

                    if event.src_path.endswith('.gtf'):
                        r = mm('deseq2',d)
                        if r == 1:
                            print('Deseq2 executed successfully')
                        else:
                            print('Deseq2 not executed')

                    if event.src_path.endswith('.csv'):
                        multithread_cnt = 1
                        return "Pipeline successfully completed"
            
                automation_event_handler.on_created = on_created        
                
                path="."
                go_recursively = True
                automation_observer = Observer()
                automation_observer.schedule(automation_event_handler, path, recursive=go_recursively)
                automation_observer.start()

                try:
                    while True:
                        if multithread_cnt == 0:
                            time.sleep(1)
                        else:
                            break
                            exit()
                            
                except KeyboardInterrupt:
                    automation_observer.stop()
                    automation_observer.join()        
            
            
            
            event_handling()'''
        else:
            return "Please check whether u have selected the correct username or not "
            
        
        return "Thank You"

if __name__=='__main__':
    app.run()
