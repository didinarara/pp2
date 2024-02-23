import re

input_string = input("Enter a string: ")

pattern = r'[A-Z][a-z]+'

matches = re.findall(pattern, input_string)

if matches:
    print("Sequences of one uppercase letter followed by lowercase letters:")
    for match in matches:
        print(match)
else:
    print("No matches found.")
