import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

app.secret_key=os.environ["SECRET_KEY"];

@app.route('/')
def renderMain():
    return render_template('home.html')
    

@app.route('/quiz')
def renderMain():
    if cq == 1:
        render_template('quiz.html', question='CHOOSE A!', correct="A", ["HI", "Bye", "This is wrong", "Bananas"])
    elif cq == 2:
        render_template('quiz.html', ASDF='')
    elif cq == 3:
        render_template('quiz.html', ASDF='')
    elif cq == 5:
        redirect('/answers')
    else redirect('/')

@app.route('/answers')
def renderMain():
    return render_template('home.html')

    
if __name__=="__main__":
    app.run(debug=False)
