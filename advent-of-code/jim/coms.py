with open('com_data.txt') as f:
    com_data: str = f.read()

strings = []
for i in range(len(com_data)-14):
    strings.append(com_data[i:i+14])

for string in strings:
    if len(string) == len(set(string)):
        print(string)
        print(f"{strings.index(string) + 14}")
        break
