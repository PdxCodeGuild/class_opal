rain_input = input('is it raining out? yes or no: ')
temp_input = input('what is the temperature outside? ')

# at this point, these are "boolean literals"
is_raining = False
is_cold = False

# each side of an and/or must be its own complete boolean evaluation
if rain_input == 'yes' or rain_input == 'y':
    # because this value is set conditionally, it is no longer a literal
    is_raining = True

if int(temp_input) < 60:
    # int casting will only work if the user puts in a number
    is_cold = True

if is_cold and is_raining:
    print(':( :( :( :(')
elif is_cold or is_raining:
    # this condition only occurs if they're *not* both true
    print(":| :| :| :| :|")
else:
    print(':) :) :) :) :) :)')


def t_or_f(arg):
    # this function returns a boolean
    return is_raining


thing = t_or_f(is_raining)  # thing is now a boolean as well
