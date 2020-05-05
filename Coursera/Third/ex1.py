from math import sqrt
a = float(input())
b = float(input())
c = float(input())
p = 0.5 * (a + b + c)
S = sqrt(p * (p - a)*(p - b)*(p - c))
print(S)
