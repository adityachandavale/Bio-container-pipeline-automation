import automate_mode
from flask import Flask,render_template,request
import manual_mode

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

        e = manual_mode.Exec(a,b)
    return e


@app.route('/Automation',methods=['POST','GET'])
def auto():
    if(request.method=='POST'):
        a = request.form['t1']
        ae = automate_mode.auto_exec(a)
        return "Thank You"

if __name__=='__main__':
    app.run()