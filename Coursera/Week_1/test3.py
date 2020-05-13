N = int(input())
hours = N // 3600 % 24
minutes = N // 60 % 60
seconds = N % 60

m1 = minutes // 10
m2 = minutes % 10

s1 = seconds // 10
s2 = seconds % 10
print(hours, ':', m1, m2, ':', s1, s2, sep='')
