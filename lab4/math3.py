from math import *


def area_regular_polygon(number, size):
    return (number * size**2) / (4 * tan(pi / number))


n, s = int(input()), float(input())
print(area_regular_polygon(n, s))
