#too lazy to refactor
from flask import Flask, render_template, request, redirect,session
import random
app = Flask(__name__)
app.secret_key='poshit'
# our index route will handle rendering our form
@app.route('/')
def index():
    try:
        session['secretNum']
    except:#initialize everything
        session['secretNum']=random.randrange(1,101)
        session['buttonTxt']='Submit'
        session['txt1']=''
    return render_template("index.html")
@app.route('/guess',methods=['POST'])
def guess():
    if int(request.form['guessNum'])==session['secretNum']:
        #session['buttonTxt']='Play Again!'
        session['color2']='green'
        session['txt2']="{} was the right number!".format(request.form['guessNum'])
        #displays the button that lets  you restart
        return redirect('/')
    elif int(request.form['guessNum'])<session['secretNum']:
        session['txt1']='too low!'
    elif int(request.form['guessNum'])>session['secretNum']:
        session['txt1']='too high!'      
    return redirect('/')
#what's left: hide text box, change color & border
@app.route('/restart')
def restart():
    session.pop('secretNum')
    return redirect('/')

app.run(debug=True)