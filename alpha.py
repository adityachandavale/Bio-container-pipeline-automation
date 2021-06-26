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
        u1 = request.form['u1']
        
        #print("Usename ",type(u1))
        #print("Filename with path ",type(fn))
        #result = find_files(fn,"/home/grp6")
        #print(result)
        #print("Result ",result)

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
                
        
        return "Thank You"

if __name__=='__main__':
    app.run()