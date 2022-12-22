from flask import Flask, render_template, request, redirect

app = Flask(__name__)

conversion_dict = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254
}


def unit_converter(distance, input_unit, output_unit):
    distance=int(distance)
    meter_conversion = conversion_dict[input_unit] * distance
    conversion2 = meter_conversion / conversion_dict[output_unit]
    return round(conversion2)


@app.route('/', methods=['GET', 'POST'])
def converted_data():

    # Make this return the user's converted number.
    if request.method == 'POST':
        # Access form inputs to pass as parameters into function
        # Which is instantiated here so we can use them as variables.
        distance = request.form["distance"]
        input_unit = request.form["input_unit"]
        output_unit = request.form["output_unit"]
        # Any variables created in this 'if' statement are available to be passed into the function
        data = unit_converter(distance, input_unit, output_unit)

        # Store "data" variable in context so it can be accessed for rendering template
        context = {
            "distance": distance,
            "input": input_unit,
            "output": output_unit,
            "data": data
        }

        print(distance)
        return render_template('lab5.html', context=context)

    return render_template('lab5.html')


app.run(debug=True)
