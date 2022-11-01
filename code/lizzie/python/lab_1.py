conversion_dict = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254
}

distance = input('What is the distance? ')

distance=int(distance)

input_unit = input('What are the input units? ')

meter_conversion = conversion_dict[input_unit] * distance

output_unit = input('What are the output units? ')

conversion2 = conversion_dict[output_unit] * meter_conversion

print(f'{distance} {input_unit} is {round(conversion2, 2)} {output_unit}.')