from functools import reduce

original_input = "4556737586899855"

# Convert the input string into a list of ints
input_string = list(map(lambda x: int(x), list(original_input)))

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
input_string = list(map(lambda x: x  - 9 if x > 9 else x, input_string))
print(input_string)

# Sum all values.
sum_of_inputs = reduce(lambda a, b: a + b, input_string)
print(sum_of_inputs)

# Take the second digit of that sum.
my_total_string = str(sum_of_inputs)

print(my_total_string[1])
print(check_digit)

# If that matches the check digit, the whole card number is valid.
if my_total_string[1] == str(check_digit):
    print("number is valid")
else:
    print("number is invalid")