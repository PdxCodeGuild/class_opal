from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method =="POST":
        abc = "abcdefghijklmnopqrstuvwxyz"
        user_word = request.form["user_word"]
        #word = request.form["user_word"]
        word = user_word.lower()
        n = request.form["n"]
        n = int(n)
        rot = lambda x: "".join([abc[(abc.find(c) + n) % 26] for c in x])
        answer = rot(word)
        return render_template('lab05.html', answer=answer) 
    return render_template('lab05.html')

app.run(debug=True)