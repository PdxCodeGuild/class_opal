# Ask the user to enter the numbers one at a time, putting them into a list. If the user enters 'done', then calculate and display the average. The following code demonstrates how to add an element to the end of a list.

# ```python
# nums = []
# nums.append(5)
# print(nums)
# ```

# Below is an example input/output:


# ```
# > enter a number, or 'done': 5
# > enter a number, or 'done': 3
# > enter a number, or 'done': 4
# > enter a number, or 'done': done
# average: 4


# nums = [5, 0, 8, 3, 4, 1, 6]
# sum_of_nums = 0

# for num in nums:
#     sum_of_nums += num

# average = sum_of_nums/len(nums)
# print(average)


num_list = []
average = sum(num_list)/len(num_list)


while True:
    user_input = input("Enter number or 'done' to quit: ")
    user_input = int(user_input)
    if user_input == 'done':
        print(f'The average is: {average}')
        break
