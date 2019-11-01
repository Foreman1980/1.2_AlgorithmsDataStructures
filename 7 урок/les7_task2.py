#    Задание № 2 урока № 7:
#    Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

from random import random

size = 10
# lst = [round(random() * 50, 2) for _ in range(size)]
lst = [24.4, 24.82, 6.99, 6.32, 39.05, 24.78, 0.95, 2.43, 46.83, 43.77]
print(lst)


def mergeSort(lst):
    def merge(lst1, lst2):  # Забыл совсем, что в методе ".pop()" можно указать индекс элемента, потом только посмотрел
        ind1 = 0            # реализацию в интернете, выгладело бы попроще, но пусть останется...тож работает
        ind2 = 0
        lst = []
        while ind1 < len(lst1) and ind2 < len(lst2):
            if lst1[ind1] < lst2[ind2]:
                lst.append(lst1[ind1])
                ind1 += 1
            else:
                lst.append(lst2[ind2])
                ind2 += 1
        lst.extend(lst1[ind1:] + lst2[ind2:])
        return lst

    resultList = []
    if len(lst) <= 1:
        return lst
    else:
        n = len(lst) // 2
        resultList = merge(mergeSort(lst[:n]), mergeSort(lst[n:]))
    return resultList


print(mergeSort(lst))

# Вывод вида -  [24.4, 24.82, 6.99, 6.32, 39.05, 24.78, 0.95, 2.43, 46.83, 43.77]
#               [0.95, 2.43, 6.32, 6.99, 24.4, 24.78, 24.82, 39.05, 43.77, 46.83]
#
#               Process finished with exit code 0
