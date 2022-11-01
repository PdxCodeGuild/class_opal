def main():
    '''convert a unit of distance given by a user to another unit of distance chosen by the user'''

    def measurement_converter(distance=1, start='ft', end='m'):
        '''convert any listed unit of distance measurement to any other'''
        # library containing meter conversions
        meter_conv_table = {
        'in': .0254,
        'ft': .3048,
        'yd': .9144,
        'm': 1,
        'km': 1000,
        'mi':1609.34,
    }
        # convert starting unit to meters
        meters = distance * meter_conv_table[start]
        # convert meters to end unit
        distance_end = meters / meter_conv_table[end]
        return distance_end


    valid_inputs = "'in', 'ft', 'yd', 'm', 'km', 'mi'"
    # get distance
    distance_start = int(input('What is the distance?\n'))
    # starting unit
    unit_start = input(f'Enter the start unit from the list below:\n{valid_inputs}\n')
    # end unit
    unit_end = input(f'\nEnter the desired end unit from the list below:\n{valid_inputs}\n')
    # convert
    distance_end = round(measurement_converter(distance_start, unit_start, unit_end), 4)
    # display answer
    print(f'\n{distance_start} {unit_start} is {distance_end} {unit_end}.')

main()