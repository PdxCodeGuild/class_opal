# Lab 05: Redo Python Lab (Unit Converter) as Flask App #User enters distance, input & output units, and app shows them conversion(m).

from flask import Flask, render_template, request, redirect
import unit_converter

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(index.html)
    ...

app.run(debug=True)