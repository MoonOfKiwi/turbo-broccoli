A, B, C = int(input()), int(input()), int(input())
D = int(input())
E = int(input())

if A <= D:
    if B <= E or C <= E:
        print('YES')
elif B <= D:
    if A <= E or C <= E:
        print('YES')
elif C <= D:
    if A <= E or B <= E:
        print('YES')
else:
    print('NO')
