# input_string = input("Please enter a string: ").lower() 
# def rot13(input_string, rotation=13):
#     abc = "abcdefghijklmnopqrstuvwxyz"
#     output = ""

#     for char in input_string:
#         print("Char: ", char)
#         input_index = abc.find(char)
#         print("Index: ", input_index)
#         output_index = (input_index - rotation)
#         print(output_index)
#         output += abc[output_index]
#     return output
# print(rot13(input_string))

#Version 2

input_string = input("Please enter a string: ").lower() #Change it to all lower right away
rotation = int(input("Please enter number of rotation: "))
def rot13(input_string, rotation):
    
    abc = "abcdefghijklmnopqrstuvwxyz"
    output = ""

    for char in input_string:
        print("Char: ", char)
        input_index = abc.find(char)
        print("Index: ", input_index)
        output_index = (input_index - rotation)
        print(output_index)
        output += abc[output_index]
    return output

print(rot13(input_string, rotation))