// Lab 2: Number to Phrase
// Convert a given number into its English representation. Handle numbers from 0-999.

let number = prompt("Please enter a number from 0 to 999: ")
number = parseInt(number)
const numberListTo19 = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}
const numberListForTeensOver100 = {
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}
const numberListByTens = {
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}
const numberListByTensOver100 = {
    1: "ten",
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety"
}
const tensPlaceNumberList = {
    0: "",
    2: "twenty-",
    3: "thirty-",
    4: "forty-",
    5: "fifty-",
    6: "sixty-",
    7: "seventy-",
    8: "eighty-",
    9: "ninety-"
}
const hundredsPlaceNumberList = {
    1: "one hundred",
    2: "two hundred",
    3: "three hundred",
    4: "four hundred",
    5: "five hundred",
    6: "six hundred",
    7: "seven hundred",
    8: "eight hundred",
    9: "nine hundred"
}
unitsPlace = number%10
tensPlace = Math.floor(number/10)
hundredsPlace = Math.floor(number/100)
hundredsRemainder = Math.floor(number%100/10)
unitsRemainder = number%100%10
teensRemainder = number%100

// Creates a conditional to print an error message for negative integers out of range.
if number < 0:
    print("Your entry is invalid.  You did not enter a number from 0 to 999.")
// Creates a conditional to print the integer "0" as a word.
elif number == 0:
    print("0 is written out as zero.")
// Creates a conditional to print integers as words if user input is 1 - 19.
elif number <= 19:
    print(f"{number} is written out as {numberListTo19[number]}.")
// Creates a conditional to print integers as words if user input is a multiple of 10, starting at 20
elif number == 20 or number == 30 or number == 40 or number == 50 or number == 60 or number == 70 or number == 80 or number == 90:
    print(f"{number} is written out as {numberListByTens[number]}.")
// Creates a conditional to print integers as words for all other user input less than 100
elif number >= 21 and number <= 99:
    print(f"{number} is written out as {tensPlaceNumberList[tensPlace]}{numberListTo19[unitsPlace]}.")
// Creates a conditional to print integers as words for all numbers from 100 to 999.
elif number >= 100 and number <= 999:
    if number == 100 or number == 200 or number == 300 or number == 400 or number == 500 or number == 600 or number == 700 or number == 800 or number == 900:
        print(f"{number} is written out as {hundredsPlaceNumberList[hundredsPlace]}")
    elif unitsRemainder == 0:
        print(f"{number} is written out as {hundredsPlaceNumberList[hundredsPlace]} {numberListByTensOver100[hundredsRemainder]}")
    elif hundredsRemainder == 1:
        print(f"{number} is written out as {hundredsPlaceNumberList[hundredsPlace]} {numberListForTeensOver100[teensRemainder]}")
    else:
        print(f"{number} is written out as {hundredsPlaceNumberList[hundredsPlace]} {tensPlaceNumberList[hundredsRemainder]}{numberListTo19[unitsRemainder]}.")
// Creates a conditional to print an error message for positive integers out of range.
else:
    print("Your entry is invalid.  You did not enter a number from 0 to 999.")