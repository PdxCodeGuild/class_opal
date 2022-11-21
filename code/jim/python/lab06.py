original_input = "4556737586899855"

# Convert the input string into a list of ints
input_string = list(original_input)

for i in range(len(input_string)):
    input_string[i] = int(input_string[i])

print(input_string)

# Slice off the last digit. That is the check digit.
check_digit = input_string.pop()
print(input_string)

# Reverse the digits.
input_string.reverse()
print(input_string)

# Double every other element in the reversed list (starting with the first number in the list).
for i in range(len(input_string)):
    if i % 2 == 0:
        input_string[i] = 2 * input_string[i]
print(input_string)

# Subtract nine from numbers over nine.
for i in range(len(input_string)):
    if input_string[i] > 9:
        input_string[i] = input_string[i] - 9
print(input_string)

# Sum all values.
my_total = 0
for i in range(len(input_string)):
    my_total += input_string[i]
print(my_total)

# Take the second digit of that sum.
my_total_string = str(my_total)

print(my_total_string[1])
print(check_digit)

# If that matches the check digit, the whole card number is valid.
if my_total_string[1] == str(check_digit):
    print("number is valid")
else:
    print("number is invalid")