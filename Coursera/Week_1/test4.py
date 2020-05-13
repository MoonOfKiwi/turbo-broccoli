H1 = int(input())
M1 = int(input())
S1 = int(input())

H2 = int(input())
M2 = int(input())
S2 = int(input())

first_moment = H1 * 3600 + M1 * 60 + S1
second_moment = H2 * 3600 + M2 * 60 + S2

print(second_moment - first_moment)
