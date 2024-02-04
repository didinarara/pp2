import math

def sphere_volume(radius):
    if radius < 0:
        return "Radius must be non-negative"
    else:
        volume = (4 / 3) * math.pi * radius**3
        return volume

radius = float(input("Enter the radius of the sphere: "))
result = sphere_volume(radius)

if type(result) == float:
    print(f"The volume of the sphere with radius {radius} is: {result:.2f} cubic units")
else:
    print(result)
