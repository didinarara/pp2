import re

input_string = input("Enter a string: ")

pattern = r'[ ,.]'

result = re.sub(pattern, ':', input_string)

print("Original string:", input_string)
print("Modified string:", result)
