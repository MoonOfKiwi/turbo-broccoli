#Вывод, вывод
formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format('раз', 'два', 'три', 'четыре'))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
        'Спят в конюшне пони,',
        'начал пес дремать,',
        'только мальчик Джонни',
        'не ложится спать!'
))
 #1)Взять строку formatter, определнную в строке 1
 #2)Вызвать ее функцию format, то есть выполнить консольную команду по имени format.
 #3)Передать функции format 4 аргумента, которые совпадают с 4-мя группами символов
 # {} в значении переменной formatter. Можно перефразировать как:
 # "передать аргуметы консольной команде format"
 #4)В результате вызова функции format для строки formatter получаем новую строку,
 # в которой символы {} заменены на 4 переменные. Этот результат выведет ффункция print.