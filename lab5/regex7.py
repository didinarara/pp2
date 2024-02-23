import re

def snake_to_camel(snake_case):
    return re.sub(r'_([a-z])', lambda match: match.group(1).upper(), snake_case)

snake_case_string = input("Enter a snake case string: ")

camel_case_string = snake_to_camel(snake_case_string.capitalize())

print("Camel case string:", camel_case_string)
