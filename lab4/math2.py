def area_trapezoid(h, a, b):
    area = (h*(a+b))/2
    return area

h = float(input("Height: "))
a = float(input("Base, first value: "))
b = float(input("Base, second value: "))

area = area_trapezoid(a, b, h)

print("Expected Output: ", area)