N = int(input())
a = int(N // 100 % 100)
b = int(N // 10 % 10)
c = int(N % 10)
sum = int(a + b + c)
print(sum)
