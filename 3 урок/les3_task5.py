#     Задание № 5 урока № 3:
#     В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
#
#     Примечания:
#     Не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.
#     Попытайтесь решить задания без использования функций max, min, sum, sorted и их аналогов, в том числе написанных
# самостоятельно.

from random import randint

myList = [randint(-10, 10) for _ in range(randint(10, 20))]
print(f'Исходный список - {myList}')

maxNegativeItem = 0
posMaxNegativeItem = 0
for i in range(len(myList)):
    if maxNegativeItem == 0 and myList[i] < 0:
        maxNegativeItem = myList[i]
        posMaxNegativeItem = i
    elif maxNegativeItem < myList[i] < 0:
        maxNegativeItem = myList[i]
        posMaxNegativeItem = i

if maxNegativeItem == 0:
    print('В данном массиве отрицательные элементы отсутствуют!')
else:
    print(f'Максимальный отрицательный элемент списка = {maxNegativeItem}, его индекс = {posMaxNegativeItem}')

# Про случай нескольких равных максимальных отрицательных значений (как здесь) условие ничего не говорит...
# Вывод вида -  Исходный список - [-10, 3, 5, -8, 10, -9, 8, -6, -8, -6, -8, 5, -8, 9, 9, -1, -1, -7, -1, -8]
#               Максимальный отрицательный элемент списка = -1, его индекс = 15
#
#               Process finished with exit code 0
