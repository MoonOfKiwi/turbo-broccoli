from math import sqrt
a = float(input())
b = float(input())
c = float(input())
D = b**2 - 4 * a * c
if D == 0:
    x1 = (-b + sqrt(D)) / (2 * a)
    if x1 % 1 == 0:
        x1 = int(x1)
    print(x1)
elif D > 0:
    x1 = (-b - sqrt(D)) / (2 * a)
    x2 = (-b + sqrt(D)) / (2 * a)
    if x1 > x2:
        (x1, x2) = (x2, x1)
    if x1 % 1 == 0:
        x1 = int(x1)
    if x2 % 1 == 0:
        x2 = int(x2)
    print(x1, x2)
