#     Задание № 9 урока № 3:
#     Найти максимальный элемент среди минимальных элементов столбцов матрицы.
#
#     Примечания:
#     Попытайтесь решить задания без использования функций max, min, sum, sorted и их аналогов, в том числе написанных
# самостоятельно.

from random import randint

myMatrix = [[randint(0, 9) for i in range(5)] for j in range(5)]
for row in myMatrix:
    print(row)

maxItem = None
for i in range(len(myMatrix[0])):
    minItem = row[0]
    for j in range(len(myMatrix)):
        if myMatrix[j][i] < minItem:
            minItem = myMatrix[j][i]
    print(f'{minItem:>2}', end=' ')
    if maxItem is None or minItem > maxItem:
        maxItem = minItem

print(f'- минимальные элементы столбцов\nМаксимальный элемент среди минимальных элементов столбцов матрицы = {maxItem}')

# Вывод вида -  [3, 5, 2, 3, 8]
#               [7, 6, 9, 4, 2]
#               [1, 9, 4, 0, 6]
#               [8, 7, 9, 4, 5]
#               [7, 7, 1, 4, 9]
#                1  5  1  0  2 - минимальные элементы столбцов
#               Максимальный элемент среди минимальных элементов столбцов матрицы = 5
#
#               Process finished with exit code 0
