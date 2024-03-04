from functools import reduce
import operator

def multiply_list(numbers):
    if not numbers:
        return None
    
    result = reduce(operator.mul, numbers)
    return result

numbers = [1, 2, 3, 4, 5]
result = multiply_list(numbers)
print("Result of multiplying all numbers:", result)
