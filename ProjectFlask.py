from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html<name>')
def myCheck():
    if(name=='Automation'):
        return render_template('Automation.html')
    else:
        return render_template('Manual.html')

if __name__=='__main__':
    app.run()