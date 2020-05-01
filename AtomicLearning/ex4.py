#Переменные и имена
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print('В наличии', cars, 'автомобилей.')
print('И только', drivers, 'водителей вышли на работу.')
print('Получается, что', cars_not_driven, 'машин пустуют.')
print('Мы можем перевезти сегодня', carpool_capacity, 'человек.')
print('Сегодня нужно отвезти', passengers, 'человек.')
print('В каждой машине будет примерно', average_passengers_per_car,'человека.')
print()
#Практические задания
#0 Ошибка NameError: name 'car_pool_capacity' is not defined означает, что
#  программа не может быть исполнена из-за отсутствия в коде переменной с таким названием.

#1-2 Число с плавающей точкой float (floating point real values — числа с плавающей точкой, дроби)
# представляют действительные числа и записываются с десятичной точкой, которая разделяет целое
# число и его дробную часть; так же могут представлять собой «scientific notation«, где E или e
# обозначают «в степени 10» (2.5e2 = 2.5 x 102 = 250); не поддерживают длинную арифметику.
# Если указать просто 4 во II строчке кода, то изменится значение carpool_capacity, которое использует перемнную space_in_a_car.
# Вместо 120.0 станет 120.

#3 Прокомментировать строчки с присвоением значения переменной.
cars = 100 # Перменной cars соответсвует значение 100.
space_in_a_car = 4 # Переменной space_in_a_car соответсвует значение 4.
drivers = 30 # Переменной drivers соответсвует значение 30.
passengers = 90 # Переменной passengers соответсвует значение 90.
cars_not_driven = cars - drivers # Переменной cars_not_driven присвоено значение
# разницы между переменными cars и drivers.
cars_driven = drivers # Переменной cars_driven соответсвует значение drivers.
carpool_capacity = cars_driven * space_in_a_car # Переменной carpool_capacity присвоено значение
# произведения переменных cars_driven и space_in_a_car.
average_passengers_per_car = passengers / cars_driven # Переменной average_passengers_per_car присвоено значение
# частного переменных passengers и cars_driven.

print('В наличии', cars, 'автомобилей.')
print('И только', drivers, 'водителей вышли на работу.')
print('Получается, что', cars_not_driven, 'машин пустуют.')
print('Мы можем перевезти сегодня', carpool_capacity, 'человек.')
print('Сегодня нужно отвезти', passengers, 'человек.')
print('В каждой машине будет примерно', average_passengers_per_car,'человека.')
print()

#4 Символ "=" называется оператором присваивания; присваивает значения, указанные справа, переменной, указанной слева.

#5 Символ "_" подчеркивания.

#6 Придуманные вычисления
x = 10
i = 7
y = 20 * x + 17 * i + (x + i)**i
print (y)

#7 Квадратное уравнение
import math
# np.sqrt(25) == 5.0
a = int(input())
b = int(input())
c = int(input())
D = int(b**2 - 4 * a * c)
y = int(a * x**2 + b * x + c)
x1 = (-b - math.sqrt(D)) / (2 * a)
x2 = (-b + math.sqrt(D)) / (2 * a)
print(x1, x2)
