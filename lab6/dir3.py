import os

def path_info(path):
    if os.path.exists(path):
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        return filename, directory
    else:
        return "Path does not exist"

path = input("Enter the path: ")

result = path_info(path)

if isinstance(result, tuple):
    filename, directory = result
    print("Path exists.")
    print("Filename:", filename)
    print("Directory:", directory)
else:
    print(result)
