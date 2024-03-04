def write_list_to_file(filename, data):
    try:
        with open(filename, 'w') as file:
            for item in data:
                file.write(str(item) + '\n')
        print(f"List has been written to '{filename}' successfully.")
    except IOError:
        print(f"Error writing to '{filename}'.")

my_list = ['apple', 'banana', 'orange', 'grape']

filename = input("Enter the filename to write the list to: ")

write_list_to_file(filename, my_list)

#open file and write that list in this file
