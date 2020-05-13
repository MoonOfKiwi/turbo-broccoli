s = input()
first_f = s.find('f')
subtitle2 = s[first_f + 1:]
second_f = subtitle2.find('f')
if first_f != -1:
    if second_f != -1:
        print(second_f + first_f + 1)
    if second_f == -1:
        print('-1')
else:
    print('-2')
