# Lab 1 - Unit Converter, Version 4

# Creates a variable that stores user input of a distance as units
user_distance = input("What is the distance (ft, mi, m, km, yd or in)? ")
# Typecasts user input to an integer for conversion
user_distance = int(user_distance)
# Creates a variable that stores user input of a starting unit of measure
units_input = input("What are the input units (ft, mi, m, km, yd, or in)? ")
# Creates a variable that stores the user's desired unit of measure as an output 
units_output = input("What are the output units (ft, mi, m, km, yd, or in)? ")
# Creates a dictionary that stores units of measure as keys and numeric conversions as values
conversion = {"ft": 0.3048, "mi": 1609.34, "m": 1, "km": 1000, "yd": 0.9144, "in": 0.0254}
# Creates a variable that converts user input of distance to meters, according to user input of
# desired starting units
new_distance = user_distance * conversion[units_input]
# Creates a variable that converts meter conversion to user input of desired output units 
new_units = new_distance / conversion[units_output]
# Displays the conversion of user's inputs of distance and unit measure to user's desired unit 
# measureoutput
print(f"{user_distance} {units_input} is {new_units} {units_output}.")