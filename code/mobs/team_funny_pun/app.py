from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_data = {
            'text': request.form['text'],
            'priority': request.form['priority']
        }
        todos['todos'].append(new_data)
        with open('db.json', 'w') as f:
            # write the data back to the data.json file
            f.write(json.dumps(todos, indent=4))
        return redirect('/')
    return render_template('index.html', todos=todos)


with open('db.json', 'r') as f:
    todos = json.load(f)
app.run(debug=True)
