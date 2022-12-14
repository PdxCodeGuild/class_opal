s = input("What letters or word do you want to encrypt? ")

n = input("Enter the cipher rotation amount (1-25): ")

n = int(n)

def rot_alpha(n):
    from string import ascii_lowercase as lc, ascii_uppercase as uc
    lookup = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: s.translate(lookup)

print(rot_alpha(n))