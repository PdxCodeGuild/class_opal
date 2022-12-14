from flask import Flask, render_template, request, redirect
app = Flask(__name__)

keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method =="POST":
        user_word = request.form["user_word"]
        rotate_number == request.form["rotate_number"]
        #print(user_word)
        working_string = ""
        for i in user_word:
            position1 = keys.index(i) #i has to be inside loop or it will return an "i is not defined" error
            if position1 >= 13:
                position2 = position1 - 13
                new_letter = keys[position2]
            else:
                position2 = position1 + 13 
                new_letter = keys[position2]
            working_string += new_letter
        return render_template('lab05.html', answer=working_string) 
    return render_template('lab05.html')

app.run(debug=True)









# Simple version: the user could just input the word to encode.
# * web form and then project
# * This lab doesn’t require styling
# * spit results back to user using one of 2 options:
#     1. use json db from mob/group lab and replace stuff as needed
#     2. instead of redirect, render template and then pass in answer=answer