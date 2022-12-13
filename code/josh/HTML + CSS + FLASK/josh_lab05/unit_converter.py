#Unit Converter

def unit_converter():
    user_distance = int(input("What is the distance (ft, mi, m, km, yd or in)? "))
    units_input = input("What are the input units (ft, mi, m, km, yd, or in)? ")
    units_output = input("What are the output units (ft, mi, m, km, yd, or in)? ")
    conversion = {"ft": 0.3048, "mi": 1609.34, "m": 1, "km": 1000, "yd": 0.9144, "in": 0.0254}
    new_distance = user_distance * conversion[units_input]
    new_units = new_distance / conversion[units_output]
    print(f"{user_distance} {units_input} is {new_units} {units_output}.")

unit_converter()