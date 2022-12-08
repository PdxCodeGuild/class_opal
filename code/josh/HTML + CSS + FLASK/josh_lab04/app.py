from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    var = 'Hello World!'
    return render_template('index.html', var=var)


app.run(debug=True)