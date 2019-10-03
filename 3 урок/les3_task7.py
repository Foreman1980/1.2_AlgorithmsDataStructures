#     Задание № 7 урока № 3:
#     В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба
# являться минимальными), так и различаться.
#
#     Примечания:
#     Попытайтесь решить задания без использования функций max, min, sum, sorted и их аналогов, в том числе написанных
# самостоятельно.

from random import randint

myList = []
print('Исходный массив значений             - ', end='')
for i in range(randint(10, 20)):
    myList.append(randint(-10, 10))
    print(f'{myList[i]:>4}', end='')

firstMinItem = myList[0]
posFirstMinItem = 0
secondMinItem = myList[1]
posSecondMinItem = 1

for i in range(len(myList)):
    if myList[i] < firstMinItem:
        secondMinItem = firstMinItem
        posSecondMinItem = posFirstMinItem
        firstMinItem = myList[i]
        posFirstMinItem = i
    elif myList[i] < secondMinItem and i != posFirstMinItem:
        secondMinItem = myList[i]
        posSecondMinItem = i

print('\nПервый и второй минимальные элементы - ', end='')
for i in range(len(myList)):
    if i == posFirstMinItem:
        print(f'{1:>4}', end='')
    elif i == posSecondMinItem:
        print(f'{2:>4}', end='')
    else:
        print('', end='    ')
print()

# Вывод вида -  Исходный массив значений             -   -7   6  10   8  -2   4   4  -5  -1   7
#               Первый и второй минимальные элементы -    1                           2
#
#               Process finished with exit code 0

# Вывод вида -  Исходный массив значений             -    3  -9   3  -2 -10   6  -2   6   1  -9   6  10  -5
#               Первый и второй минимальные элементы -        2           1
#
#               Process finished with exit code 0

# Вывод вида -  Исходный массив значений             -   -9   5  -8  -9   6  -9  -2  -2  -4  -5  -9  -1   3  -6  -3   2  -4
#               Первый и второй минимальные элементы -    1           2
#
#               Process finished with exit code 0
