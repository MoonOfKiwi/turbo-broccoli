#Дополнительно о переменных и выводе
my_name = 'Зед Шоу'
my_age = 35 # это правда!
my_height = 188 # см
my_weight = 80 # кг
my_eyes = 'Голубые'
my_teeth = 'Белые'
my_hair = 'Каштановые'

print(f'Давайте поговорим о человеке по имени {my_name}.')
print(f'Его рост составляет {my_height} см.')
print(f'Он весит {my_weight} кг.')
print('На самом деле это не так много.')
print(f'У него {my_eyes} глаза и {my_hair} волосы.')
print(f'Его зубы обычно {my_teeth}, хотя он и любит пить кофе.')

# эта строка кода доволно сложная не ошибитесь!
total = my_age + my_height + my_weight
print(f'Если я сложу {my_age}, {my_height} и {my_weight}, то получу {total}.')
print()

#1 Изменить имена всех переменных
name = 'Николай'
age = 23 # это правда!
height = 180 # см
weight = 87 # кг
eyes = 'Серые'
teeth = 'Белые'
hair = 'Русые'

print(f'Давайте поговорим о человеке по имени {name}.')
print(f'Его рост составляет {height} см.')
print(f'Он весит {weight} кг.')
print('На самом деле это не так много.')
print(f'У него {eyes} глаза и {hair} волосы.')
print(f'Его зубы обычно {teeth}, хотя он и любит пить кофе.')

# эта строка кода доволно сложная не ошибитесь!
total = age + height + weight
print(f'Если я сложу {age}, {height} и {weight}, то получу {total}.')
print()

#2 Программа преобразующая см в м, кг в т.
print('Введите свой вес в кг:', end=' ')
weight_a = int(input())
weight_b = weight_a / 1000 # в тоннах
print(f'Тогда ваш вес в тоннах равен: {weight_b}.')
print()
print('А какой у вас рост в см?', end=' ')
height_a = int(input())
height_b = height_a / 100 # в метрах
print(f'Ваш рост в метрах составляет {height_b}.')

#3 f-строки выглядят как: f'Какой-нибудь текст {переменная}. Пора форматровать! Помести эти переменные в строки!
