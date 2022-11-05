ones_digits = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
tens_digits = {0: "", 10: "ten", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}
hundreds = {0: "", 100: " one hundred", 200: "two hundred",300: "three hundred", 400: "four hundred", 500: "five hundred", 600: "six hundred", 700: "seven hundred", 800: "eight hundred", 900: "nine hundred"}
teens = {}
num = int(input("Enter a number: "))
def convert_to_words(number):    
    if num < 20:
        return ones_digits[num]
    
    elif num >20 and num < 100:
        return tens_digits[(num//10)*10]+ " " + ones_digits[num%10]
    
    elif num >= 100 and num < 1000:    
        if (num % 100)//10 == 0:
            return hundreds[(num//100)*100] + " " + ones_digits[num%10]
        elif (num % 100):
            if num % 100 < 20:
                return hundreds[(num//100)*100] + " " + ones_digits[(num%100)]
        return hundreds[(num//100)*100] + " " + tens_digits[((num%100)//10)*10] + " " + ones_digits[(num%10)]
print(convert_to_words(num))


#version 3

hundreds = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
tens = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
ones = ["","I","II","III","IV","V","VI","VII","VIII","IX"]

def convert_to_roman():
    if num < 1000 and num:
        return hundreds[num//100] + tens[(num%100)//10] + ones[num%10]
print(convert_to_roman())




        
    
     
        


     
