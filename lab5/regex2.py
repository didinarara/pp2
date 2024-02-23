import re

pattern = r'ab{2,3}'

input_string = input("Enter a string: ")

if re.fullmatch(pattern, input_string):
    print("String matches the pattern: 'a' followed by two to three 'b's.")
else:
    print("String does not match the pattern.")
