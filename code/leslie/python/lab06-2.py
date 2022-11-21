from functools import reduce
cc = '4556737586899855'

def cc_validator():
    cc_num = list(map(lambda i: int(i), cc))
    check_digit = cc_num.pop()
    cc_num.reverse()
    doubled_even_nums = [cc_num[i] *2 if i%2 == 0 else cc_num[i] for i in range(len(cc_num))]
    minus_nine = list(map(lambda i: doubled_even_nums[i]-9 if doubled_even_nums[i] > 9 else doubled_even_nums[i], range(len(doubled_even_nums))))
    sum_of_minus_nine = sum(minus_nine)
    if str(check_digit) == str(sum_of_minus_nine)[1]:
        print("Valid!")
    else:
        print("Invalid. Contacting authorities.")
cc_validator()   
    

    