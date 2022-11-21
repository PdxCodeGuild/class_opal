meter_conversions = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000
    }

distance = int(input("what is the distance? "))
units = input("What are the units? ")

def convert_to_meters(distance, units):
    return meter_conversions[units] * distance

distance_in_meters = convert_to_meters(distance, units)

print(f"{distance} {units} is {round(distance_in_meters,4)} m")
