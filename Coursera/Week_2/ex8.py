A, B, C = int(input()), int(input()), int(input())
D = int(input())
E = int(input())
if A > B:
    (A, B) = (B, A)
if B > C:
    (B, C) = (C, B)
if A > B:
    (A, B) = (B, A)
if D > E:
    (D, E) = (E, D)
if A <= D and B <= E:
    print('YES')
else:
    print('NO')
