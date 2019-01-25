import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

app.secret_key=os.environ["SECRET_KEY"];

class quest:
    question=''
    correct=''
    options=[]
    
    def __init__(self, ques_, corr_, opti_):
        self.question = ques_
        self.correct = corr_
        self.options=opti_

questArr = [quest('CHOOSE A', 'A', ["HI", "Bye", "This is wrong", "Bananas"]), quest('THE FITNESS GRAM PACER TEST', 'B', ["HI", "Bye", "This is wrong", "Bananas"]),quest('TOMMOROW', 'C', ["HI", "Bye", "This is wrong", "Bananas"])]

@app.route('/')
def renderMain():
    return render_template('home.html')
    

@app.route('/quiz')
def renderQuiz():
    render_template('quiz.html', quest = questArr[0])
"""
    if cq == 1:
        render_template('quiz.html', quest= questArr[0])
    elif cq == 2:
        render_template('quiz.html', quest= questArr[1])
    elif cq == 3:
        render_template('quiz.html', quest= questArr[2])
    elif cq == 5:
        redirect('/answers')
    else redirect('/')
    """
    

@app.route('/answers')
def renderAnswers():
    return render_template('home.html')

    
if __name__=="__main__":
    app.run(debug=False)
