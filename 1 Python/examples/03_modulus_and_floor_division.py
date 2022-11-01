'''
Fritz is a baker, he makes donuts and sells them by the dozen.
For a given number of donuts that he has
- how many dozens can he sell?
- how many will he have left over?
'''

total_donuts = 1501
dozen_size = 12


number_of_dozens = total_donuts // dozen_size
leftover_donuts = total_donuts % dozen_size

print(number_of_dozens)
print(leftover_donuts)


# string formatting

output = f'Fritz can sell {number_of_dozens} dozen donuts and will have {leftover_donuts} left over'
print(output)

# accessing a list by index
this_list = ['zero', 'one', 'two']
print(this_list[0])
print(this_list[1])

# accessing a dict by key
this_dict = {
    1: 'one',
    2: 'two',
    'one': 1
}

print(this_dict[1])
print(this_dict[2])
print(this_dict['one'])
print(this_dict.get(1))
