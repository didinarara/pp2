from functools import reduce

numbers = [1, 2, 3, 4, 5]

def multiply(x, y):
    return x * y

result = reduce(multiply, numbers)

print("Multiplication of all numbers:", result)
