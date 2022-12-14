from flask import Flask, render_template, request, redirect
import json

from rot_cipher import get_encoding

app = Flask(__name__)


# This route handles GET requests *only*
@app.route('/')
def index():
    return render_template('index.html', context=cipher_context)


# This route handles POST requests *only*
@app.route('/submit-cipher-request/', methods=['POST'])
def handle_submit():
    # the request.form dictionary object contains the form data
    # keys are whatever you put as the "name attribute" on the form inputs
    new_data = {
        "user_string": request.form['user_string'],
        "rotation_amount": request.form['rotation_amount'],
        "encoded_string": get_encoding(request.form['user_string'], request.form['rotation_amount'])
    }

    # Adds our new dictionary (made with form data!) to the global variable
    cipher_context['ciphers'].append(new_data)

    # use a filepath relative to wherever your terminal is pointed when you run this app
    with open(r'data.json', 'w') as f:
        # write the data back to the data.json file
        f.write(json.dumps(cipher_context, indent=4))

    # Redirects back to the root/index route
    return redirect('/')

    # Do this if you want to render a different route from the form submission route
    # but with new / different context
    # return render_template('index.html', context=cipher_context)


# Whenever this app loads, it reads the data.json file
# and makes its context available as a global dictionary
with open(r'data.json', 'r') as f:
    cipher_context = json.load(f)

app.run(debug=True)
