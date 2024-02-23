import re

def split_at_uppercase(string):
    return re.findall(r'[A-Z][^A-Z]*', string)

input_string = input("Enter a string: ")

result = split_at_uppercase(input_string)

print("Result after splitting at uppercase letters:", result)
