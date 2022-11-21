dic_of_measurement_in_meters = {
    'ft' : 0.3048,
    'mi' : 1609.34,
    'm' : 1,
    'km' : 1000,
    'yrd' : 0.9144,
    'in' : 0.0254,
}

distance_question = input('What is the distance? ')
unit_question = input('What are the units? ')
unit_output_question= input('What are the output in units? ')
total_measurements= int(distance_question) * dic_of_measurement_in_meters[unit_question]
total_measurements_of_output= int(total_measurements) / dic_of_measurement_in_meters[unit_output_question]
print(f"{distance_question} {unit_question} is {total_measurements_of_output} {unit_output_question}")

