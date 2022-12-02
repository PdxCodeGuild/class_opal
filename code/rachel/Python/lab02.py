x = input('Enter a number: ')
x = int(x)
hundreds_digit = x//100
y = hundreds_digit*100
ones_digit = x%10
tens_digit = x-(y+ones_digit)

def charlie(hundreds_digit):
    if hundreds_digit == 0:
        return('')
    elif hundreds_digit == 1:
        return('one hundred ')
    elif hundreds_digit == 2:
        return('two hundred ')
    elif hundreds_digit == 3:
        return('three hundred ')
    elif hundreds_digit == 4:
        return('four hundred ')
    elif hundreds_digit == 5:
        return('five hundred ')
    elif hundreds_digit == 6:
        return('six hundred ')
    elif hundreds_digit == 7:
        return('seven hundred ')
    elif hundreds_digit == 8:
        return('eight hundred ')
    elif hundreds_digit == 9:
        return('nine hundred ')
def alpha(tens_digit):
    if tens_digit == 10:
        return('ten-')
    elif tens_digit == 20:
        return('twenty-')
    elif tens_digit == 30:
        return('thirty-')
    elif tens_digit == 40:
        return('forty-')
    elif tens_digit == 50:
        return('fifty-')
    elif tens_digit == 60:
        return('sixty-')
    elif tens_digit == 70:
        return('seventy-')
    elif tens_digit == 80:
        return('eighty-')
    elif tens_digit == 90:
        return('ninety-')
def beta(ones_digit):
    if ones_digit == 2:
        return('two-')
    elif ones_digit == 3:
        return('three')
    elif ones_digit == 4:
        return('four')
    elif ones_digit == 5:
        return('five')
    elif ones_digit == 6:
        return('six')
    elif ones_digit == 7:
        return('seven')
    elif ones_digit == 8:
        return('eight')
    elif ones_digit == 9:
        return('nine')

if x == 10:
    print('ten')
elif x == 11:
    print('eleven')
elif x == 12:
    print('twelve')
elif x == 13:
    print('thirteen')
elif x == 14:
    print('fourteen')
elif x == 15:
    print('fifteen')
elif x == 16:
    print('sixteen')
elif x == 17:
    print('seventeen')
elif x == 18:
    print('eighteen')
elif x == 19:
    print('nineteen')
else:
    print(f'{charlie(hundreds_digit)}{alpha(tens_digit)}{beta(ones_digit)}')
    




