from flask import Flask, render_template

app = Flask(__name__)


STUDENTS = [
    "Jim",
    "Lizzie",
    "Hayato",
    "Nick",
    "Josh",
    "Leslie",
    "Rachel",
]


def triple_number(n):
    return n*3


@app.route("/")
def index():
    # class_name = "Opal"
    # bootcamp_name = "Intensive Full-Stack Development Bootcamp"
    # school = "PDX Code Guild"
    # return render_template('index.html', num_students=len(STUDENTS), class_name=class_name, school=school, bootcamp_name=bootcamp_name)

    context = {
        "class_name": "Opal",
        "school_info": {
            "school": "PDX Code Guild",
            "bootcamp_name": "Intensive Full-Stack Development Bootcamp",
        },
        "num_students": len(STUDENTS),
        "students": STUDENTS,
        "lucky_numbers": [13, 4, 7],
        "triple_number": triple_number
    }
    return render_template('index.html', context=context)


@app.route('/instructor')
def instructor():
    return "This class is taught by Danny"


@app.route('/student/<string:student_name>/<string:last_init>')
def student_page(student_name, last_init):
    if student_name.title() in STUDENTS:
        return f"{student_name.title()} {last_init.upper()} is a student in Class Opal"
    return f"{student_name} is not a student in Class Opal"


app.run(debug=True)
