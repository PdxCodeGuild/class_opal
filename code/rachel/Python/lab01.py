#Version 1
""""""
meter = float(0.3048)
unit = input("Enter the number of feet: ")
unit = int(unit)
total_meters = unit * meter
print(f'{unit} feet is equal to {total_meters:.2f} meters.')
""""""
#Version 2 & 3
""""""
Conversions = {
    'inch': 0.0254,
    'feet': 0.3048,
    'yard': 0.9144,
    'mile': 1609.34,
    'meter': 1,
    'km': 1000
}
unit = input('Enter the type of units you want to convert: ')
distance = input('Enter the distance you want to convert: ')
unit_converter = Conversions[unit]
distance = int(distance)
total_distance = distance * unit_converter
print(f'{distance} {unit} is equal to {total_distance:.2f} meters.')
""""""
#Version 4
""""""
Conversions = {
    'feet': 0.3048,
    'mile': 1609.34,
    'meter': 1,
    'km': 1000
}
distance = input('Enter the distance you want to convert: ')

unit = input('Enter the type of units you want to convert: ')
unit_converter = Conversions[unit]
distance = int(distance)
conversion1 = distance * unit_converter

#print(f'{distance} {unit} is equal to {conversion1:.2f} meters.')

output_unit = input('Enter the type of units you want to convert to: ')
unit_converter2 = Conversions[output_unit]
total_distance = conversion1 / unit_converter2
print(f'{distance} {unit} is equal to {total_distance:.2f} {output_unit}.')
""""""