import math

def degrees_to_radians(degrees):
    radians = degrees * (math.pi / 180)
    return radians

degrees = float(input("Input degree: "))

radians = degrees_to_radians(degrees)

print("Output radian:", radians)
