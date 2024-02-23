import re

input_string = input("Enter a string: ")

pattern = r'[a-z]+_[a-z]+'

matches = re.findall(pattern, input_string)

if matches:
    print("Sequences of lowercase letters joined with an underscore:")
    for match in matches:
        print(match)
else:
    print("No matches found.")
