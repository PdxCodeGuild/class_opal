with open(r'C:\Users\jbrennan\Google Drive\Architecture\Tests\pdx_code_guild\fullstack_bootcamp\class_opal\advent-of-code\jim\dir_data.txt') as f:
    dir_data: str = f.read()

dir_data = dir_data.split('\n')

dir_dict = {'/': [[], 0]}

current_dict = ''

for line in dir_data:
    if line == '$ cd /':
        current_dict = '/'
        pass
    elif line == '$ cd ..':
        current_dict = current_dict.rsplit('/', 1)[0]
    elif line[0:5] == '$ cd ':
        if current_dict == '/':
            current_dict += line[5:]
        else:
            current_dict += '/' + line[5:]
        if current_dict not in dir_dict.keys():
            dir_dict[current_dict] = [[], 0]
    elif line[0:3] == 'dir':
        dir_dict[current_dict][0].append(line[4:])
    elif line == '$ ls':
        pass
    else:
        dir_dict[current_dict][1] += int(line.split(' ')[0])

dir_file_size_totals = {}
for dir in dir_dict.keys():
    dir_file_size_totals[dir] = dir_dict[dir][1]


# dir_size_total = {}
# for dir in dir_dict.keys():
#     dir_size_total[dir] = dir_file_size_totals[dir]
#     for sub_dir in dir_dict[dir][0]:
#         if dir == '/':
#             dir_size_total[dir] += dir_file_size_totals[dir + sub_dir]
#         else:
#             dir_size_total[dir] += dir_file_size_totals[dir + '/' + sub_dir]

dir_size_total = {}
for dir in dir_dict.keys():
    dir_size_total[dir] = dir_file_size_totals[dir]
    for sub_dir in dir_file_size_totals.keys():
        if sub_dir.startswith(dir) and sub_dir != dir:
            dir_size_total[dir] += dir_file_size_totals[sub_dir]

answer = 0
for dir in dir_size_total:
    if dir_size_total[dir] <= 100_000:
        answer += dir_size_total[dir]

print(dir_dict)
print(dir_file_size_totals)
print(dir_size_total)
print(answer)

total_available_space = 70000000
required_unused_space = 30000000
current_used_space = dir_size_total['/']
current_unused_space = total_available_space - current_used_space
required_size_reduction = required_unused_space - current_unused_space

print(current_used_space)
print(current_unused_space)
print(required_size_reduction)

dir_size_list = []
for dir in dir_size_total.keys():
    dir_size_list.append(dir_size_total[dir])

dir_size_list = sorted(dir_size_list)

print(dir_size_list)

min_val = min(i for i in dir_size_list if i > required_size_reduction)

print(min_val)
