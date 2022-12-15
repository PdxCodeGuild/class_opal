from flask import Flask, render_template, request, redirect

app = Flask(__name__)

data = [{'input_string': 'abcdefg',
         'rotation': 3,
         'new_string': 'xyzabcd'},
        {'input_string': 'hello',
         'rotation': 12,
         'new_string': 'vszzc'}]


@app.route('/')
def index():
    return render_template('index.html', data=data)


def rot13(input_string, rotation):
    abc = "abcdefghijklmnopqrstuvwxyz"
    output = ''

    for char in input_string:
        input_index = abc.find(char)
        output_index = (input_index - rotation)
        output += abc[output_index]
    return output


@app.route('/submit/', methods=['POST'])
def handle_submit():
    new_string = rot13(request.form['input_string'],
                       int(request.form['rotation']))
    new_data = {
        'input_string': request.form['input_string'],
        'rotation': request.form['rotation'],
        'new_string': new_string
    }
    print('new string:', new_string)
    data.append(new_data)
    return render_template('index.html', data=data, new_string=new_string)


app.run(debug=True)
