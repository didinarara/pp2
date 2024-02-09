import math

def area_of_regular_polygon(n, s):
    apothem = s / (2 * (math.tan(math.pi/n)))
    perimeter = n * s
    area = (apothem * perimeter) / 2
    return int(area)

n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))

result = area_of_regular_polygon(n, s)

print("The area of the polygon is: ", result)