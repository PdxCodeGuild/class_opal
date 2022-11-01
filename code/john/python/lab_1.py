# Instructions
'''
This lab will involve writing a program that allows the user to convert a number between units.

Each version should be accomplished 
using a dictionary and each must be completed without the use of if/elif statements.

You do NOT need to use a while loop

'''



# VERSION 1
'''
Ask the user for the number of feet, and print out the equivalent distance in meters.

Hint: 1 ft is 0.3048 m.

So we can get the output in meters by multiplying 
the input distance by 0.3048. Below is some sample input/output.
'''
# this all might get pushed back. See about use of WHILE LOOPS
# you could use a while loop in a while loop
# VERSION 1

# ft_meters_dict = {
#     'ft': 0.3048 
#     }

# user_input_ft = input('What is the distance in feet? ')
# user_input_ft = int(user_input_ft)
# ft_meters_conversion = user_input_ft * ft_meters_dict['ft']

# print(round(ft_meters_conversion))


# VERSION 2
'''
Allow the user to also enter the units. Then depending on the units, 
convert the distance into meters. 
The units we'll allow are feet, miles, meters, and kilometers.
'''

# meter_conversion_dict = {
#     'feet' : 0.3048, 
#     'mile': 1609.34, 
#     'meter': 1, 
#     'kilometer': 1000, 
#     }
# user_distance_input = input('What is the distance? ')
# user_distance_input = int(user_distance_input)    
# user_unit_input = input('What are the units? Enter feet, mile, meter, or kilometer: ')

# conversion_meters = user_distance_input * meter_conversion_dict[user_unit_input]
# print(round(conversion_meters))

# # VERSION 3
# '''
# Add support for yards, and inches.
# '''

# meter_conversion_dict = {
#     'feet' : 0.3048, 
#     'mile': 1609.34, 
#     'meter': 1, 
#     'kilometer': 1000, 
#     'yard': 0.9144,
#     'inch': 0.0254,
#     }
# user_distance_input = input('What is the distance? ')
# user_distance_input = int(user_distance_input)    
# user_unit_input = input('What are the units? Enter inch, feet, yard, mile, meter, or kilometer: ')

# conversion_meters = user_distance_input * meter_conversion_dict[user_unit_input]
# print(round(conversion_meters))

# Version 4

user_distance_input = int(input('What is the distance? '))  
user_unit_input = input('What are the units? Enter inch, feet, yard, mile, meter, or kilometer: ')
user_output_input = input('Enter what you want the output unit to be in: ')

meter_conversion_dict = {
    'feet' : round(0.3048 * user_distance_input, 4), 
    'mile': round(1609.34 * user_distance_input, 4), 
    'meter': round(1 * user_distance_input, 4), 
    'kilometer': round(1000 * user_distance_input, 4), 
    'yard': round(0.9144 * user_distance_input, 4),
    'inch': round(0.0254 * user_distance_input, 4),
    }

convert_output_dict = {
    'feet' : round(meter_conversion_dict[user_unit_input] / 0.3048, 4), 
    'mile': round(meter_conversion_dict[user_unit_input] / 1609.34, 4), 
    'meter': round(meter_conversion_dict[user_unit_input] / 1, 4), 
    'kilometer': round(meter_conversion_dict[user_unit_input] / 1000, 4), 
    'yard': round(meter_conversion_dict[user_unit_input] / 0.9144, 4),
    'inch': round(meter_conversion_dict[user_unit_input] / 0.0254, 4),
    }
final_result = convert_output_dict[user_output_input]

print(f'{user_distance_input} {user_unit_input} is {final_result} {user_output_input}')

# print(round(conversion_meters))

# first convert everything to meters. Done. 
# get the units for the output


'''
## Version 4

Now we'll ask the user for the distance, the starting units, 
and the units to convert to.

You can think of the values for the conversions 
as elements in a matrix, where the rows will be 
the units you're converting from, and the columns 
will be the units you're converting to. 
Along the horizontal, the values will be 1 (1 meter is 1 meter, 
1 foot is 1 foot, etc).

|  | ft  | mi  | m  | km  |
|---|----|----|----|---|
|ft|1||0.3048||
|mi||1|1609.34||
|m|1/0.3048|1/1609.34|1|1/1000|
|km|||1000|1|

But instead of filling out that matrix, and checking for 
each pair of units (`if from_units == 'mi' and to_units == 'km'`),
we can just convert any unit to meters, then convert the 
distance in meters to any other unit.


Furthermore you can convert them from meters by dividing a 
distance (in meters) by those same values used above. 
So first convert from the input units **_to_** meters, 
then convert **_from_** meters to the output units.

Below is some sample input/output:

```
> what is the distance? 100
> what are the input units? ft
> what are the output units? mi
100 ft is 0.0189394 mi


'''