from functools import reduce
input_string = input("Please enter a credit card number: ")

# 1Convert the input string into a list of ints
list_from_input = list(input_string)

'''what map is replacing:
list_of_ints = [int(i) for i in list_of_ints]'''
list_of_ints = list(map(lambda x: int(x), list_from_input))
check_digit = list_of_ints.pop()

# 3Reverse the digits.
list_of_ints.reverse()

# 4Double every other element in the reversed list (starting with the first number
#  in the list).
for i in range(len(list_of_ints)):
    if i % 2 == 0:
        list_of_ints[i] = 2 * list_of_ints[i]

# 5Subtract nine from numbers over nine.
'''what map is replacing:
for i in range(len(list_of_ints)):
    if list_of_ints[i] > 9:
        list_of_ints[i] = list_of_ints[i] - 9
print(list_of_ints)'''
new_list_of_ints = map(lambda x: x - 9 if x > 9 else x, list_of_ints)

# # 6Sum all values.
'''What reduce is replacing:
sum_ints = sum(new_list_of_ints)'''
sum_ints = reduce(lambda a, b: a+b, new_list_of_ints)

# 7Take the second digit of that sum.
sum_ints = str(sum_ints)

# If that matches the check digit, the whole card number is valid.
# have to cast check_digit as a string to ensure they're both able to be compared.
if sum_ints[1] == str(check_digit):
    print("Valid card!")
else:
    print("Not a valid card.")