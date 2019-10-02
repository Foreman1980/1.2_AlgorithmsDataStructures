#     Задание № 6 урока № 3:
#     В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами
# минимальный и максимальный элементы в сумму не включать.
#
#     Примечания:
#     Попытайтесь решить задания без использования функций max, min, sum, sorted и их аналогов, в том числе написанных
# самостоятельно.

from random import randint

myList = []
print('Исходный массив значений            - ', end='')
for i in range(randint(10, 20)):
    myList.append(randint(-10, 10))
    print(f'{myList[i]:>4}', end='')

posMinItem = posMaxItem = 0
minItem = maxItem = myList[0]

for i in range(len(myList)):
    if myList[i] > maxItem:
        maxItem = myList[i]
        posMaxItem = i
    if myList[i] < minItem:
        minItem = myList[i]
        posMinItem = i

# Необязательная часть...захотелось сделать указатели...
print('\nМаксимальный и минимальный элементы - ', end='')
pointer = ''
for i in range(len(myList)):
    if i == posMinItem or i == posMaxItem:
        print(f'{chr(5839):>4}', end='')
    else:
        print('', end='    ')

if posMinItem > posMaxItem:
    posMinItem, posMaxItem = posMaxItem, posMinItem

summa = 0
for i in range(posMinItem + 1, posMaxItem):
    summa += myList[i]
print(f'\nИскомая сумма элементов = {summa}')

# Вывод вида -  Исходный массив значений            -    9   7   8  -5  -1  -6  -8  -1  -2   1   6
#               Максимальный и минимальный элементы -    ᛏ                       ᛏ
#               Искомая сумма элементов = 3
#
#               Process finished with exit code 0
