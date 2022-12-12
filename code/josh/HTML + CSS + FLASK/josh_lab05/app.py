# Lab 05: Redo Python Lab (Unit Converter) as Flask App #User enters distance, input & output units, and app shows them conversion(m).

from flask import Flask, render_template
import unit_converter.py

app = Flask(__name__)

def index():
    ...