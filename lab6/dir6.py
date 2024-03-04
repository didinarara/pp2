import string

def generate_files():
    # generate files from A.txt to Z.txt
    for letter in string.ascii_uppercase:
        filename = letter + ".txt"
        with open(filename, "w") as file:
            file.write(f"This is file {filename}\n")

generate_files()
