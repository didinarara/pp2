import re

def insert_spaces(string):
    result = re.sub(r'([a-z])([A-Z])', r'\1 \2', string)
    return result

input_string = input("Enter a string: ")

result_string = insert_spaces(input_string)

print("String with spaces inserted:", result_string)
