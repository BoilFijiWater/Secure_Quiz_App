import os
from flask import Flask, url_for, render_template, request
from flask import session

app = Flask(__name__)

app.secret_key=os.environ["SECRET_KEY"];

#question class
class quest:
    question=''
    correct=''
    options=[]
    
    def __init__(self, ques_, corr_, opti_):
        self.question = ques_
        self.correct = corr_
        self.options = opti_

#Array/List of "quest(ion)" objects 
questArr = [
    quest('Whats the the square root of PI/3', 'A', ["0.591", "0.675", "0.635", "0.257"]), 
    quest('What has a head and a tail but no legs', 'B', ["four is a lie", "coin", "ghost", "kangaroo"]),
    quest("What's the best pet", 'C', ["Dogs", "Baby Chameleon ", "Raccoon", "All of the above"])
]

@app.route('/')
def renderMain():
    session.clear()
    return render_template('home.html')

@app.route('/quiz', methods=["POST", "GET"])
def renderQuiz():
    if "answers" not in session:
        session["answers"] = {}
    if "cq" not in session:
        session["cq"] = 0
    cq = session["cq"]

    if "selected" in request.form:
        if not request.form["selected"] == {}:
            session["answers"][str(cq)]= request.form["selected"]
            session["cq"] += 1
            cq += 1

    if cq >= len(questArr):
        score, answerReveal = getScore(session["answers"])
        maxSc = len(questArr)

        return render_template('score.html', maxScore=maxSc, score=score, answerReveal=answerReveal)
    return render_template('quiz.html', quest = questArr[cq])

def getScore(answ):
    answerReveal = [False]*len(questArr)
    total = 0
    for i in range(len(answ)):
        if questArr[i].correct == answ[str(i)]:
            answerReveal[i] = True
            total += 1
    return total, answerReveal


if __name__=="__main__":
    app.run(debug=False)
