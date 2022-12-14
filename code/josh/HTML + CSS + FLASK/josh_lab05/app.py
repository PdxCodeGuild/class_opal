# Lab 05: Redo Python Lab (Unit Converter) as Flask App

from flask import Flask, render_template, request, redirect
from unit_converter import unit_converter as converter

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', context=converter)


@app.route('/', methods=['GET', 'POST'])
def handle_submit():
    if request.method == 'POST':
        user_data = {
        'user_distance': request.form['user_distance'],
        'units_input': request.form['units_input'],
        'units_output': request.form['units_output']
        }
        unit_converter = converter(user_data['user_distance'], user_data['units_input'], user_data['units_output'])

    return render_template('index.html', context=unit_converter)
   

app.run(debug=True)