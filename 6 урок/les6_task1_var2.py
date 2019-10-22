#    Задание № 1 урока № 6 вариант № 2:
#    1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
# уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
#
#    Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
#    a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
#    b. написать 3 варианта кода (один у вас уже есть);
#
#    проанализировать 3 варианта и выбрать оптимальный;
#
#    c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с
# кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
#    d. написать общий вывод: какой из трёх вариантов лучше и почему.
#    Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof после каждой переменной, а проявили
# творчество, фантазию и создали универсальный код для замера памяти.

import sys

sizeCount = 0 # будет глобальной переменной

def sizeCounter(x):
    global sizeCount
    print(f'{sys.getsizeof(x)} ', end='')
    sizeCount += sys.getsizeof(x)
    if hasattr(x, '__iter__'):  # проверка является ли объект итерируемым
        if hasattr(x, 'items'):  # проверка является ли объект словарём
            for xx in x.items():
                sizeCounter(xx)
        elif not isinstance(x, str):
            for xx in x:
                sizeCounter(xx)


print(sys.version, sys.platform)
# 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)] win32

myList = [1, -6, 5, 7, 2, -9, -7, -5, -6, 4, -5, 3] # Первое слагаемое

modaList = [] # список для хранения уникальных значений
countModaList = [] # список для суммирования кол-ва вхождений уникальных значений. Соответсвие с первым по индексам
for i in myList: # Значение "i" возьмём в конце исполнения программы
    if i not in modaList:
        modaList.append(i)
        countModaList.append(1)
    else:
        countModaList[modaList.index(i)] += 1

print(f'Исходный список                          - {myList}')
print(f'Уникальные значения исходного списка     - {modaList}') # Второе слагаемое
print(f'Количество вхождений уникальных значений - {countModaList}') # Третье слагаемое

maxCount = 0
for i in countModaList:
    if i > maxCount:
        maxCount = i # "maxCount" четвёртое слагаемое

print(f'Список самых "популярных" значений       - ', end='')
for i in countModaList: # возьмём последнее хранящееся в "i" значение как пятое слагаемое
    if maxCount == i:
        print(f' {modaList[countModaList.index(i)]} ', end='')
        countModaList[countModaList.index(i)] = 1

print('\n\nПервое слагаемое (Bites):    ', end='')
sizeCounter(myList)
print(f'\nПодитог = {sizeCount if sizeCount < 1024 else round(sizeCount / 1024, 2)}' + ('Kb' if sizeCount > 1024 else 'B'))

print('Второе слагаемое (Bites):    ', end='')
sizeCounter(modaList)
print(f'\nПодитог = {sizeCount if sizeCount < 1024 else round(sizeCount / 1024, 2)}' + ('Kb' if sizeCount > 1024 else 'B'))

print('Третье слагаемое (Bites):    ', end='')
sizeCounter(countModaList)
print(f'\nПодитог = {sizeCount if sizeCount < 1024 else round(sizeCount / 1024, 2)}' + ('Kb' if sizeCount > 1024 else 'B'))

print('Четвёртое слагаемое (Bites): ', end='')
sizeCounter(maxCount)
print(f'\nПодитог = {sizeCount if sizeCount < 1024 else round(sizeCount / 1024, 2)}' + ('Kb' if sizeCount > 1024 else 'B'))

print('Пятое слагаемое (Bites):     ', end='')
sizeCounter(maxCount)
print(f'\n\nВсего задействовано памяти = {sizeCount if sizeCount < 1024 else round(sizeCount / 1024, 2)}' + 'KB' if sizeCount > 1024 else 'B')

# Вывод вида -  3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)] win32
#
#               Исходный список                          - [1, -6, 5, 7, 2, -9, -7, -5, -6, 4, -5, 3]
#               Уникальные значения исходного списка     - [1, -6, 5, 7, 2, -9, -7, -5, 4, 3]
#               Количество вхождений уникальных значений - [1, 2, 1, 1, 1, 1, 1, 2, 1, 1]
#               Список самых "популярных" значений       -  -6  -5
#
#               Первое слагаемое (Bites):    160 28 28 28 28 28 28 28 28 28 28 28 28
#               Подитог = 496B
#               Второе слагаемое (Bites):    192 28 28 28 28 28 28 28 28 28 28
#               Подитог = 968B
#               Третье слагаемое (Bites):    192 28 28 28 28 28 28 28 28 28 28
#               Подитог = 1.41Kb
#               Четвёртое слагаемое (Bites): 28
#               Подитог = 1.43Kb
#               Пятое слагаемое (Bites):     28
#
#               Всего задействовано памяти = 1.46KB
#
#               Process finished with exit code 0
