meter_conversions = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254
    }

distance = int(input("what is the distance? "))
input_units = input("What are the input units? ")
output_units = input("What are the output units? ")

def convert_to_meters(distance, input_units):
    return meter_conversions[input_units] * distance

def convert_from_meters(distance, output_units):
    return distance / meter_conversions[output_units]

distance_in_meters = convert_to_meters(distance, input_units)
distance_in_output_units = convert_from_meters(distance_in_meters, output_units)

print(f"{distance} {input_units} is {round(distance_in_output_units, 7)} {output_units}")
