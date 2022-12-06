## Lab 3 Version 1

# nums = [5, 0, 8, 3, 4, 1, 6]
# sum_of_nums = 0

# for num in nums:
#     sum_of_nums += num

# average = sum_of_nums/len(nums)
# print(average)


## Lab 3 Version 2

num_list = []

while True:
    user_input = input("Enter number or 'done' to quit: ")
    if user_input == 'done':
        print(f'The average is: {average}')
        break
    else:
        user_input = int(user_input)
        num_list.append(user_input)
        average = sum(num_list)/len(num_list)