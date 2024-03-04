import os

def check_access(path):
    #test existence
    if not os.path.exists(path):
        return f"Path '{path}' does not exist."
    
    #test readability
    if not os.access(path, os.R_OK):
        return f"No read access to '{path}'."
    
    #test writability
    if not os.access(path, os.W_OK):
        return f"No write access to '{path}'."
    
    #test executability (for directories)
    if os.path.isdir(path) and not os.access(path, os.X_OK):
        return f"No execute access to '{path}' (for directories)."
    
    return f"Access to '{path}' is allowed."

path = input("Enter the path to check access: ")

access_result = check_access(path)
print(access_result)
