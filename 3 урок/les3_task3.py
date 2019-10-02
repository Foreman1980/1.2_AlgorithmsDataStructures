#     Задание № 3 урока № 3:
#     В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
#
#     Примечания:
#     Попытайтесь решить задания без использования функций max, min, sum, sorted и их аналогов, в том числе написанных
# самостоятельно.

from random import randint

myList = [randint(-10, 10) for _ in range(randint(10, 20))]
print(myList)
minItem = maxItem = myList[0]
posMinItem = posMaxItem = 0
for i in range(len(myList)):
    if myList[i] > maxItem:
        maxItem = myList[i]
        posMaxItem = i
    if myList[i] < minItem:
        minItem = myList[i]
        posMinItem = i
print(f'Минимальное значение массива = {minItem}, максимальное = {maxItem}\nПоменяем их местами:')
spam = myList[posMinItem]
myList[posMinItem] = myList[posMaxItem]
myList[posMaxItem] = spam
print(myList)

# Про случай нескольких равных минимальных и максимальных значений (как здесь) условие ничего не говорит...
# Вывод вида -  [0, 2, -8, -7, -8, -4, -4, 9, 5, 1, 9, 8, 6, 0]
#               Минимальное значение массива = -8, максимальное = 9
#               Поменяем их местами:
#               [0, 2, 9, -7, -8, -4, -4, -8, 5, 1, 9, 8, 6, 0]
#
#               Process finished with exit code 0