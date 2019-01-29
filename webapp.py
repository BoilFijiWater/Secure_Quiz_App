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

questArr = [
    quest('Whats the the square root of PI/3', 'A', ["0.591", "0.675", "0.635", "0.257"]), 
    quest('What has a head and a tail but no legs', 'B', ["four is a lie", "coin", "ghost", "kangaroo"]),
    quest("What's the best pet", 'C', ["Dogs", "Baby Chameleon ", "Raccoon", "All of the above"])
    ]

@app.route('/')
def renderMain():
    return render_template('home.html')
    

@app.route('/quiz', methods=["POST", "GET"])
def renderQuiz():
    if "cq" not in session:
        print("cq not in session")
        session["cq"] = 0
    if "answers" not in session:
        session["answers"] = {}
    
    print("selected" in request.form)
    """ if "selected" in request.form:
       session["answers"][session["cq"]] = request.form["selected"] """
    """ print(type(session["cq"]))
    print(type(len(questArr))) """
    if session["cq"] < len(questArr):
        session["cq"] = session["cq"] + 1
        return render_template('quiz.html', quest = questArr[session["cq"]-1])
    else:
        return redirect('/answers')

@app.route('/answers')
def renderAnswers():
    print(session["answers"])
    session.clear()
    return render_template('home.html')

    
if __name__=="__main__":
    app.run(debug=False)
