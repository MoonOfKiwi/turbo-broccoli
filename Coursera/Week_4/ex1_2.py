from math import sqrt
x1, y1 = float(input()), float(input())
x2, y2 = float(input()), float(input())
x3, y3 = float(input()), float(input())


def distance(x1, y1, x2, y2):
    return sqrt(((x2 - x1)**2) + ((y2 - y1)**2))

p1 = distance(x1, y1, x2, y2)
p2 = distance(x1, y1, x3, y3)
p3 = distance(x2, y2, x3, y3)
print(p1 + p2 + p3)
