#Получение ответов на вопросы?
print('Сколько тебе лет?', end=' ')
age = input()
print('Каков твой рост?', end=' ')
height = input()
print('Сколько ты весишь?', end=' ')
weight = input()

print(f'Итак, тебе {age} лет, в тебе {height} см роста и {weight} кг веса.')
print()

#3 Свой код
print('Сколько ты покупаешь шоколадок в неделю?', end=' ')
bar = int(input())
print('Сколько стоит одна шоколадка?', end=' ')
cost = int(input())
sum = bar * cost

print(f'Тогда купив {bar} шоколадок по цене {cost} рублей, мы потратим {sum} рублей.')
