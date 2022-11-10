input_string = input("Please enter a credit card number: ")

# 1Convert the input string into a list of ints
list_of_ints = list(input_string)

list_of_ints = [int(i) for i in list_of_ints]
print(list_of_ints)

# 2Slice off the last digit. That is the check digit.
check_digit = list_of_ints.pop()
print(list_of_ints)

# 3Reverse the digits.
list_of_ints.reverse()
print(list_of_ints)

# 4Double every other element in the reversed list (starting with the first number
#  in the list).
for i in range(len(list_of_ints)):
    if i % 2 == 0:
        list_of_ints[i] = 2 * list_of_ints[i]
print(list_of_ints)

# 5Subtract nine from numbers over nine.
for i in range(len(list_of_ints)):
    if list_of_ints[i] > 9:
        list_of_ints[i] = list_of_ints[i] - 9
print(list_of_ints)

# Sum all values.
sum_ints = sum(list_of_ints)
print(sum_ints)

# Take the second digit of that sum.
# casting sum_ints as a string to be able to retrieve index
sum_ints = str(sum_ints)
print(sum_ints[1])
print(check_digit)

# If that matches the check digit, the whole card number is valid.
# have to cast check_digit as a string to ensure they're both able to be compared.
if sum_ints[1] == str(check_digit):
    print("Valid card!")
else:
    print("Not a valid card.")