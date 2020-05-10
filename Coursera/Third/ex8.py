a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())
if a != 0:
    y = (a * f - c * e) / (a * d - c * b)
    x = (e - b * y) / a
else:
    y = e / b
    x = (f - d * y) / c

if y % 1 == 0:
    y = int(y)
if x % 1 == 0:
    x = int(x)
print(x, y)
