from flask import Flask,render_template,request
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
    return ("<html><b>"+a+"</b></html> Container executed succesfully with query <html><b>"+b+"</b></html>")

def find_files(filename, search_path):
    result = ""
    for file in os.listdir(filename):
        if file.endswith(search_path):
            result = os.path.join(filename, file)
            print("function result",result)
    return result


@app.route('/Automation',methods=['POST','GET'])
def auto():
    if(request.method=='POST'):
        
        i=0
        multithread_cnt = 0
        
        a = request.form['t1']
        b = request.form['t2']
        c = request.form['t3']
        u1 = request.form['u1']
        
        #print("Usename ",type(u1))
        #print("Filename with path ",type(fn))
        #result = find_files(fn,"/home/grp6")
        #print(result)
        #print("Result ",result)

        #if(find_files(u1,".fna")):
        if(a==None or a==" "):
            r=mm('hisat',"hisat2-build '"+find_files("/home/grp6/"+u1,".fna")+"' output")
            print("hisat2 executed with command hisat2-build '",find_files("/home/grp6/"+u1,".fna"),"' output")
        else:
            r=mm('hisat',"hisat2-build '"+find_files("/home/grp6/"+u1,".fna")+"' output "+a)
            print("hisat2 executed with command hisat2-build '",find_files("/home/grp6/"+u1,".fna"),"' output ",a)
        if r == 1:
            r2 = mm('hisat2',b)
            print('Hisat2 executed successfully')
            if(r2 == 1):
                r3 = mm('stringtie',c)
                print('Stringtie executed successfully')
                if(r3 == 1):
                    return "hisat2 executed with command hisat2-build '/home/grp6/",u1,"/",find_files("/home/grp6/"+u1,".fna"),"' output"
                
        
        return "hisat2 executed with command hisat2-build '/home/grp6/",u1,"/",find_files("/home/grp6/"+u1,".fna"),"' output"

if __name__=='__main__':
    app.run()