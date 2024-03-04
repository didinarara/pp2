def copy_file(source_file, destination_file):
    try:
        #open the source file for reading
        with open(source_file, 'r') as source:
            #read the contents of the source file
            contents = source.read()

        #open the destination file for writing
        with open(destination_file, 'w') as destination:
            #write the contents to the destination file
            destination.write(contents)

        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print(f"One of the files '{source_file}' or '{destination_file}' not found.")

source_file = input("Enter the source file: ")
destination_file = input("Enter the destination file: ")

copy_file(source_file, destination_file)
