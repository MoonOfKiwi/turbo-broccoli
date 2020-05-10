x = float(input())
integer_part = int(x // 1)
remainder_of_the_division = x % 1
if remainder_of_the_division < 0.5:
    print(integer_part)
else:
    print(integer_part + 1)
