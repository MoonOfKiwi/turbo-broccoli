from math import sqrt
a = float(input())
b = float(input())
c = float(input())
D = b**2 - 4 * a * c
x1 = (-b + sqrt(D)) / 2 * a
x2 = (-b - sqrt(D)) / 2 * a
if x1 != x2:
    if x1 > x2:
        (x1, x2) = (x2, x1)
else:
    if x1 == x2:
        (x1, x2) = (x1, '')
    if x1 == 0 and x2 == 0:
        print('')
print(x1, x2)
