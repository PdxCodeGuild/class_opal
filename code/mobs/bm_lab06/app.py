from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('list.html', context=todo_context)


@app.route('/submit-todo/', methods=['POST'])
def handle_submit():
    new_data = {
        'text': request.form['todo-item'],
        'priority': request.form['priority'],
        'todo_id': len(todo_context['todos']) + 1
    }

    todo_context['todos'].append(new_data)

    with open('data.json', 'w') as f:
        f.write(json.dumps(todo_context, indent=4))

    return redirect('/')


@app.route('/delete-todo/', methods=['POST'])
def handle_delete():

    print(request.form)

    for todo in todo_context['todos']:
        if todo['todo_id'] == int(request.form['todo-number']):
            del todo_context['todos']

    with open('data.json', 'w') as f:
        f.write(json.dumps(todo_context, indent=4))

    return redirect('/')


with open('data.json', 'r') as f:
    todo_context = json.load(f)

app.run(debug=True)
