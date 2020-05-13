string = input()
first = string.find('f')
last0 = string[::-1].find('f')
if string.find('f') != -1:
    last = len(string) - last0 - 1
    if first != last:
        print(first, last)
    if first == last:
        print(first)
