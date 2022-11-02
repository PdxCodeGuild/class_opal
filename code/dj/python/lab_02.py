num_dict = {
    0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
    11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
    19: 'Nineteen'
}

num_dict2 = {
    2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty', 7: 'Seventy', 8: 'Eighty',
    9: 'Ninety'
}

num_dict3 = {
    1: 'One hundred', 2: 'two hundred', 3: 'Three hundred', 4: 'Four hundred', 5: 'Five hundred', 6: 'Six hundred', 7: 'Seven hundred', 8: 'Eight hundred',
    9: 'Nine hundred'
}

num = 500

hundreds_digit = num // 100
print(hundreds_digit)
tens_digit = num // 10
print(tens_digit)
ones_digit = num % 10
print(ones_digit)

if num > 99:
    tens = num % 100
    if tens < 20:
        print(f"{num_dict3[hundreds_digit]}-{num_dict[tens]}")
    else:
        tens_digit = tens // 10
        print(tens)
        if num_dict[ones_digit] == 'Zero':
            print(f"{num_dict3[hundreds_digit]} {num_dict2[tens_digit]}")
        else:
            print(
                f"{num_dict3[hundreds_digit]} {num_dict2[tens_digit]}-{num_dict[ones_digit]}")
elif num < 20:
    print(num_dict[num])
else:
    if num_dict[ones_digit] == 'Zero':
        print(f"{num_dict2[tens_digit]}")
    else:

        print(f"{num_dict2[tens_digit]}-{num_dict[ones_digit]}")
