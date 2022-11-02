# nums = [5,0,8,3,4,1,6]
# total = 0

# for num in nums:
#     total += num

# avg = total/len(nums)
# print(avg)

nums = []
total = 0


while True:
    next_num = input("enter a number, or 'done': ")
    if next_num == 'done':
        break
    else:
        try:
            nums.append(float(next_num))
            total += float(next_num)

        except ValueError:
            print("Input invalid")
if len(nums) == 0:
    print("WTF??") 
else:
    avg = total/len(nums)
    print(avg)
