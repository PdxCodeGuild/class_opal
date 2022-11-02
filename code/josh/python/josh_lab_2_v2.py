# Lab 2: Number to Phrase
# Convert a given number into its English representation. Handle numbers from 0-999.


# Creates a variable to store user input
number = input("Please enter a number from 0 to 999: ")
# Creates a variable to convert user input from string to integer
number = int(number)
# Creates a dictionary to pair integer keys with their word values 1 - 19
number_list_to_19 = {
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
# Creates a dictionary to pair integert keys with their word values for numbers 11 - 19 over 100
number_list_for_teens_over_100 = {
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

# Creates a dictionary to pair integer multiples of ten as keys with their word values
number_list_by_tens = {
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}
# Creates a dictionary to pair integer multiples of ten (for nubmers > 100) as keys with their word values
number_list_by_tens_over_100 = {
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
# Creates a dictionary to pair the key of the result of floor division with the tens place word value
tens_place_number_list = {
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
# Creates a dictionary to pair the key of the result of floor division with the hundreds place word value
hundreds_place_number_list = {
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
# Creates a variable to store a single digit remainder in units place 
units_place = number%10
# Creates a varible to store a single digit as a representation of the tens place
tens_place = number//10
# Creates a variable to store a single digit as a representation of the hundreds place
hundreds_place = number//100
# Creates a variable to store a single digit as a representation of the remainder in the tens place 
hundreds_remainder = number%100//10
# Creates a variable to store a single digit as a representation of the remainder in the units place
units_remainder = number%100%10
# Creates a variable to store remainders less than 100
teens_remainder = number%100

# Creates a conditional to print an error message for negative integers out of range.
if number < 0:
    print("Your entry is invalid.  You did not enter a number from 0 to 999.")
# Creates a conditional to print the integer "0" as a word.
elif number == 0:
    print("0 is written out as zero.")
# Creates a conditional to print integers as words if user input is 1 - 19.
elif number <= 19:
    print(f"{number} is written out as {number_list_to_19[number]}.")
# Creates a conditional to print integers as words if user input is a multiple of 10, starting at 20
elif number == 20 or number == 30 or number == 40 or number == 50 or number == 60 or number == 70 or number == 80 or number == 90:
    print(f"{number} is written out as {number_list_by_tens[number]}.")
# Creates a conditional to print integers as words for all other user input less than 100
elif number >= 21 and number <= 99:
    print(f"{number} is written out as {tens_place_number_list[tens_place]}{number_list_to_19[units_place]}.")
# Creates a conditional to print integers as words for all numbers from 100 to 999.
elif number >= 100 and number <= 999:
    if number == 100 or number == 200 or number == 300 or number == 400 or number == 500 or number == 600 or number == 700 or number == 800 or number == 900:
        print(f"{number} is written out as {hundreds_place_number_list[hundreds_place]}")
    elif units_remainder == 0:
        print(f"{number} is written out as {hundreds_place_number_list[hundreds_place]} {number_list_by_tens_over_100[hundreds_remainder]}")
    elif hundreds_remainder == 1:
        print(f"{number} is written out as {hundreds_place_number_list[hundreds_place]} {number_list_for_teens_over_100[teens_remainder]}")
    else:
        print(f"{number} is written out as {hundreds_place_number_list[hundreds_place]} {tens_place_number_list[hundreds_remainder]}{number_list_to_19[units_remainder]}.")
# Creates a conditional to print an error message for positive integers out of range.
else:
    print("Your entry is invalid.  You did not enter a number from 0 to 999.")


#Git Add, Commit & Push:
#> git add files-to-be-added
#> git commit -m "your commit message goes here"
#> git push -u origin your-name/python/lab01
#Then go to the repository to create a PR.