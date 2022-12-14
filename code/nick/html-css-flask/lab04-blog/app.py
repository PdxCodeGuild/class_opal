from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", context=article_context)


with open('code/nick/html-css-flask/lab04-blog/db.json', 'r') as f:
    article_context = json.load(f)


app.run(debug=True)
