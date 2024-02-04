from math import pi

def value_of_sphere(r):
    return (4/3) * pi * r**3

R = int(input())

print(value_of_sphere(R))