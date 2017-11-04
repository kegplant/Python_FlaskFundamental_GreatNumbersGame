#too lazy to refactor
from flask import Flask, render_template, request, redirect,session
import random
app = Flask(__name__)
app.secret_key='poshit'
# our index route will handle rendering our form
@app.route('/')
def index():
    try:
        session['inputPos']
    except:
        session['inputPos']="-20px"
    try:
        session['secretNum']
    except:#initialize everything
        session['secretNum']=random.randrange(1,101)
        session['buttonTxt']='Submit'
        session['txt1']=''
        session['txt2']=''
        session['color2']='white'
        session['inputPos']="-20px"
    try:
        session['color']
    except:
        session['color']='red'
    return render_template("index.html")
@app.route('/guess',methods=['POST'])
def guess():
    try:
        session['restart']
    except:
        session['restart']=False
    if session['restart']==True:
        session.pop('secretNum')
        session.pop('restart')
        return redirect('/')
    if int(request.form['guessNum'])==session['secretNum']:
        session['buttonTxt']='Play Again!'
        # session['color']='green'
        session['txt2']="{} was the right number!".format(request.form['guessNum'])
        session['txt1']=''
        session['color2']='green'
        session['inputPos']='-1000px'
        #displays the button that lets  you restart
        session['restart']=True
    elif int(request.form['guessNum'])<session['secretNum']:
        session['txt1']='too low!'
        session['color']='red'
    elif int(request.form['guessNum'])>session['secretNum']:
        session['txt1']='too high!'  
        session['color']='red'    
    return redirect('/')
#what's left: hide text box, change color & border

# @app.route('/restart')
# def restart():
#     session.pop('secretNum')
#     return redirect('/')

app.run(debug=True)