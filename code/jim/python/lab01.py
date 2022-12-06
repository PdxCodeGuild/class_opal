meter_conversions = {'ft': 0.3048}

distance = int(input("what is the distance in feet? "))

def convert_to_meters(distance):
    return meter_conversions['ft'] * distance

distance_in_meters = convert_to_meters(distance)

print(f"{distance} ft is {round(distance_in_meters,4)} m")
