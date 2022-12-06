cc = '4556737586899855'

def cc_validator():
    cc_num = [int(i) for i in cc] 
    # print(cc_num)
    check_digit = cc_num.pop()
    # print("Check digit: ", check_digit)
    cc_num.reverse()
    # print(cc_num)
    doubled_even_nums = [cc_num[i] *2 if i%2 == 0 else cc_num[i] for i in range(len(cc_num))]
    # print(doubled_even_nums)
    minus_nine = [doubled_even_nums[i]-9 if doubled_even_nums[i] > 9 else doubled_even_nums[i] for i in range(len(doubled_even_nums))]   
    sum_of_minus_nine = sum(minus_nine)
    if str(check_digit) == str(sum_of_minus_nine)[1]:
        print("Valid!")
    else:
        print("Invalid. Contacting authorities.")
cc_validator()   
    





#1. Convert the input string into a list of ints
#print(cc_num)

# print("Check digit: ", check_digit)
#3. Reverse the digits (line 5)
# print(cc_num)
#4. Double every other element in the reversed list (starting with the first number in the list).
# print(doubled_even_nums)
#5. Subtract nine from numbers over nine.
# print(minus_nine)

# print("Sum: ", sum_of_minus_nine)
#7. Take the second digit of that sum.
#8. If that matches the check digit, the whole card number is valid.

    