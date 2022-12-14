abc = "abcdefghijklmnopqrstuvwxyz"
word = input("What letters or word do you want to encrypt? ")
n = int(input("Enter the cipher rotation amount (1-25): "))

rot = lambda x: "".join([abc[(abc.find(c) + n) % 26] for c in x])

print(rot(word))