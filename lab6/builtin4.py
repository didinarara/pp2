import time
import math

def calculate_square_root_after_milliseconds(number, milliseconds):
    time.sleep(milliseconds / 1000)  
    result = math.sqrt(number)
    return result

number = int(input(""))
milliseconds = int(input(""))

square_root = calculate_square_root_after_milliseconds(number, milliseconds)

print(f"Square root of {number} after {milliseconds} milliseconds is {square_root}")
