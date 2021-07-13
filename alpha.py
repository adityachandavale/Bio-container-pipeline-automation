from flask import Flask,render_template,request
import webbrowser
from manual_mode import manual_mode as mm
import os
import os.path


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
    return ("<html><b>"+a+"</b></html> Container executed succesfully with query(if files are not created then check the input file path or terminal) <html><b>"+b+"</b></html>")

def find_files(filename, search_path):
    result = ""
    for file in os.listdir(filename):
        if file.endswith(search_path):
            result = os.path.join(filename, file)
    print("function result",result)
    return result

def hisat2_first(a,u1):
    result = find_files("/home/query/"+u1,".fna")
    if(a==None or a==" "):
        c1 = "hisat2-build \'"+result+"\' \'/home/query/"+u1+"/Output/output\'"
        print("C1 is",c1)
        r=mm('hisat2',c1)
        print("hisat2 executed with command ",c1)
    else:
        c1 = "hisat2-build \'"+result+"\' \'/home/query/"+u1+"/Output/output\' "+a
        print("C1 is",c1)
        r=mm('hisat2',c1)
        print("hisat2 executed with command ",c1)
    return "hisat2 executed with command "+c1

def hisat2_second(b,u1):
    result = find_files("/home/query/"+u1,".fastq")
    if(b==None or b==" "):
        c1 = "hisat2 -x \'/home/query/"+u1+"/Output/output\' -U \'"+result+"\' --threads 2 --no-unal -S \'/home/query/"+u1+"/Output/output.sam\'"
        print("C1 is",c1)
        r2 = mm('hisat2',c1)
        print('Hisat2 executed successfully')
    else:
        c1 = "hisat2 -x \'/home/query/"+u1+"/Output/output\' -U \'"+result+"\' --threads 2 --no-unal -S \'/home/query/"+u1+"/Output/output.sam\' "+b
        print("C1 is",c1)
        r2 = mm('hisat2',c1)
        print('Hisat2 executed successfully')
    return "hisat2 executed with command "+c1

def stringtie_first(c,u1):
    result = find_files("/home/query/"+u1+"/Output",".sam")
    '''os.system("samtools view -bS "+result+">\'/home/query/"+u1+"/Output/out.bam\'")
    os.system("samtools sort -@ N \'/home/query/"+u1+"/Output/out.bam\'>\'/home/query/"+u1+"/Output/out.bam\'")
    os.system("samtools index \'/home/query/"+u1+"/Output/out.bam\' \'/home/query/"+u1+"/Output/output\'")
    result = find_files("/home/query/"+u1+"/Output",".bam")'''
    if(c==None or c==" "):
        c1 = "stringtie \'"+result+"\' -o \'/home/query/"+u1+"/Output/out.gtf\'"
        print("C1 is",c1)
        r2 = mm('stringtie',c1)
        print('Stringtie executed successfully')
    else:
        c1 = "stringtie \'"+result+"\' -o \'/home/query/"+u1+"/Output/out.gtf\' "+c
        print("C1 is",c1)
        r2 = mm('stringtie',c1)
        print('Stringtie executed successfully')
    return "stringtie executed with command "+c1
                                   
@app.route('/Automation',methods=['POST','GET'])
def auto():
    if(request.method=='POST'):
        
        i=0
        multithread_cnt = 0
        
        a = request.form['t1']
        b = request.form['t2']
        c = request.form['t3']
        u1 = request.form['u1']
        
        path = os.path.join("/home/query/"+u1, "Output")
        try:
            os.mkdir(path)
            print("Folder is being created at ",path)
        except OSError as error:
            print(error)
         
        result1 = hisat2_first(a,u1)
        result2 = hisat2_second(b,u1)
        result3 = stringtie_first(c,u1)
        return result1+"<br>"+result2+"<br>"+result3
    
if __name__=='__main__':
    url = 'http://127.0.0.1:5000'
    webbrowser.open_new(url)
    app.run()
  
  
  
  
  
  
  
