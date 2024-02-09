def area_of_parallelogram(b, h):
    area = b * h
    return float(area)

b = float(input("Length of base: "))
h = float(input("Height of parallelogram: "))

result = area_of_parallelogram(b, h)

print("Expected Output: ", result)