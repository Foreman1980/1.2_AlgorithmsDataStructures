# Задание № 3 урока № 1:
#     Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
#     Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ от 'a' до 'f',
# то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
#
#     Примечания:
#     Во всех заданиях, где речь идёт о буквах алфавита, решения необходимы только для строчных букв латинского алфавита от a до z.
#     Попытайтесь решить задания без использования циклов и собственных функций (они будут рассматриваться на уроке 2), а также без
# массивов (они будут рассматриваться на уроке 3).
#     Для простоты понимания зарезервированные слова forи while считаются циклом, def - функцией, любые квадратные скобки [ и ] - массивами.
# Их наличие в коде расценивается как неверное решение.


from random import randint, uniform

print('''Выберите вариант для генерации случайного значения из диапазона:
  Случайное целое число - 1
  Случайное вещественное число - 2
  Случайный символ - 3''')
var = input('Ваш выбор? ')
if var == '1':
    x, y = input('Задайте начальное и конечное значения диапазона (через пробел): ').split()
    print(f'Случайное целое число - {randint(int(x), int(y) + 1)}')
elif var == '2':
    x, y = input('Задайте начальное и конечное значения диапазона (через пробел): ').split()
    print(f'Случайное вещественное число - {uniform(float(x), float(y))}')
else:
    x, y = input('Задайте начальный и конечный символ (через пробел): ').split()
    print(f'Случайный символ - {chr(randint(ord(x), ord(y)))}')
