def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            line_count = 0
            for line in file:
                line_count += 1
        return line_count
    except FileNotFoundError:
        return f"File '{filename}' not found."

filename = input("Enter the filename: ")

lines = count_lines(filename)
if isinstance(lines, int):
    print(f"Number of lines in '{filename}': {lines}")
else:
    print(lines)
