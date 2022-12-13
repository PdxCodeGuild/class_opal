#Unit Converter

def unit_converter(user_distance, units_input, units_output):
    user_distance = int(user_distance)
    conversion = {"ft": 0.3048, "mi": 1609.34, "m": 1, "km": 1000, "yd": 0.9144, "in": 0.0254}
    new_distance = user_distance * conversion[units_input]
    new_units = new_distance / conversion[units_output]
    return {'user_distance': user_distance,
            'units_input': units_input,
            'new_distance': new_distance,
            'new_units': new_units
    }