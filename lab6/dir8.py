import os

def check_access_and_delete_file(path):
    try:
        #check if the path exists
        if not os.path.exists(path):
            print(f"File '{path}' does not exist.")
            return
        
        #check for access
        if not os.access(path, os.W_OK):
            print(f"No write access to '{path}'.")
            return
        
        #delete the file
        os.remove(path)
        print(f"File '{path}' has been deleted successfully.")
    except FileNotFoundError:
        print(f"File '{path}' not found.")
    except PermissionError:
        print(f"No permission to delete '{path}'.")

path = input("Enter the path of the file to delete: ")

check_access_and_delete_file(path)
