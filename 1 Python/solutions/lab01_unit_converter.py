conversions = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254
}

num = None
while num is None:
    try:
        num = float(input('How many units? '))
    except ValueError:
        print('Please enter a number')

num_in_m = None
while num_in_m is None:
    try:
        starting_unit = input('What units are you starting with? ')
        num_in_m = num * conversions[starting_unit]
    except KeyError:
        print('That is not a valid option')

converted = None
while converted is None:
    try:
        output_unit = input('What unit are we converting to? ')
        converted = num_in_m / conversions[output_unit]
    except KeyError:
        print('That is not a valid option')

print(f'{num} {starting_unit} is {converted} {output_unit}')
