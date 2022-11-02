#Version1

# feet = int(input("What is the distance in feet? "))
# meters = feet * 0.3048
# print(feet, "feet is", float(meters), "meters")

# #Version2
# distance = int(input("What is the distance? "))
# units = input("What are the units? ")
# if units == "meters":
#     meters = distance
# elif units == "feet":
#     meters = distance * .3048
# elif units == "miles":
#     meters = distance / 1609
# elif units == "kilometers":
#     meters = distance * 1000
# print(int(distance),units,"equals",meters,"meters")

# #Version 3
# distance = int(input("What is the distance? "))
# units = input("What are the units? ")
# if units == "meters":
#     meters = distance
# elif units == "feet":
#     meters = distance * .3048
# elif units == "miles":
#     meters = distance * 1609
# elif units == "kilometers":
#     meters = distance * 1000
# elif units == "yards":
#     meters = distance / 1.094
# elif units == "inches":
#     meters = distance / 39.37

# print(int(distance),units,"equals",meters,"meters")

#Version 4
distance = int(input("What is the distance? "))
from_units= input("What are the units? ")
to_units = input("What unit are you converting to? ")
if from_units == "meters":
    meters = distance
elif from_units == "feet":
    meters = distance * .3048
elif from_units == "miles":
    meters = distance * 1609
elif from_units == "kilometers":
    meters = distance * 1000
    
if to_units == "meters":
    converted_distance = meters
elif to_units == "feet":
    converted_distance = meters / .0348
elif to_units == "miles":
    converted_distance = meters / 1609.34
elif to_units == "kilometers":
    converted_distance = meters / 1000
   
print(int(distance),from_units,"equals",converted_distance,to_units)  
