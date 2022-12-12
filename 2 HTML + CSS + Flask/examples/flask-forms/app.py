from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)


# This route handles both GET and POST requests
@app.route('/color/', methods=['GET', 'POST'])
def color_picker():
    color = '#3c4'

    # if it's a POST request, it changes the page context
    # based on the submitted form data
    if request.method == 'POST':
        color = request.form['color']

    return render_template('color.html', color=color)


# This route handles GET requests *only*
@app.route('/')
def index():
    return render_template('index.html', context=pet_context)


# This route handles POST requests *only*
@app.route('/submit-pet/', methods=['POST'])
def handle_submit():
    # the request.form dictionary object contains the form data
    # keys are whatever you put as the "name attribute" on the form inputs
    new_data = {
        'pet': request.form['pet'],
        'species': request.form['species'],
        'person': request.form['person']
    }
    # Adds our new dictionary (made with form data!) to the global variable
    pet_context['pets'].append(new_data)

    # use a filepath relative to wherever your terminal is pointed when you run this app
    with open('2 HTML + CSS + Flask/examples/flask-forms/data.json', 'w') as f:
        # write the data back to the data.json file
        f.write(json.dumps(pet_context, indent=4))

    # Redirects back to the root/index route
    return redirect('/')

    # Do this if you want to render a different route from the form submission route
    # but with new / different context
    return render_template('index.html', context=pet_context)


# Whenever this app loads, it reads the data.json file
# and makes its context available as a global dictionary
with open('2 HTML + CSS + Flask/examples/flask-forms/data.json', 'r') as f:
    pet_context = json.load(f)

app.run(debug=True)
