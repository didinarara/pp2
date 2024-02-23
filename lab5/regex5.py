import re

pattern = r'a.*b$'

input_string = input("Enter a string: ")

if re.fullmatch(pattern, input_string):
    print("String matches the pattern: 'a' followed by anything, ending in 'b'.")
else:
    print("String does not match the pattern.")
