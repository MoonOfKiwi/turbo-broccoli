n = int(input())
nMax = n
i = 0
while n != 0:
    if n > nMax:
        nMax = n
        i = 1
    elif n == nMax:
        i += 1
    n = int(input())
print(i)
