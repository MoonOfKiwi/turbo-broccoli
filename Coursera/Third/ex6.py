P, X, Y = int(input()), int(input()), int(input())
total_sum = (X + (Y / 100)) * (1 + P / 100)
integer_part = int(total_sum // 1)
remainder_of_the_division = int((total_sum % 1)*100.00001)
print(integer_part, remainder_of_the_division)
