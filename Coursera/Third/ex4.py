price = float(input())
rubles = int(price // 1)
pennies = round((price % 1) * 100)
print(rubles, pennies)
