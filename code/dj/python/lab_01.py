metric_units = {
    "ft": 0.3048,
    "mi": 1609.34,
    "m": 1,
    "km": 1000,
    "yd": 0.9144,
    "in": 0.0254

}

distance = input(f"> what is the distance?: ")

distance = int(distance)

unit = input(f"what are the units?: ")

meters_per = metric_units[unit]

conversion = distance * meters_per

print(f"{distance} {unit} is {round(conversion, 2)} m")
