from flask import Flask, render_template, request, redirect

app = Flask(__name__)


def measurement_converter(distance=1, start='ft', end='m'):
    '''convert any listed unit of distance measurement to any other'''
    # library containing meter conversions
    meter_conv_table = {
        'in': .0254,
        'ft': .3048,
        'yd': .9144,
        'm': 1,
        'km': 1000,
        'mi': 1609.34,
    }
    # convert starting unit to meters
    meters = distance * meter_conv_table[start]
    # convert meters to end unit
    distance_end = meters / meter_conv_table[end]
    return distance_end


@app.route("/", methods=['GET', 'POST'])
def index():
    result = ""
    print('aaa')
    if request.method == 'POST':
        result = measurement_converter(
            int(request.form["distance"]), request.form["start-unit"], request.form["end-unit"])
        print(request.method)
    return render_template("index.html", context=result)


app.run(debug=True)
