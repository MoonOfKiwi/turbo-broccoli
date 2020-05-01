x = int(input())
y = int(input())
if x > y:
    print(1)
else:
    if x < y:
        print(2)
    else:
        print(0)

#Второй вариант
x = int(input())
y = int(input())
if x > y:
    print(1)
elif x < y:
    print(2)
else:
    print(0)
