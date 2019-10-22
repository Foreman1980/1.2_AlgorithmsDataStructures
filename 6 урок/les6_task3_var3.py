#    Задание № 1 урока № 6 вариант № 3 - высосанный из пальца...:
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
print(f'Исходный список                          - {myList}')

modaList = [] # список для хранения уникальных значений
countModaList = []  # список для суммирования кол-ва вхождений уникальных значений. Предполагается обратное соответсвие с
                    # первым списком по индексам
for i in range(len(myList) - 1, -1, -1): # Значение "i" возьмём в конце исполнения программы
    if myList[i] not in modaList:
        modaList.append(myList.pop()) # обрезаем исходный список...для экономии памяти
        countModaList.append(1)
    else:
        countModaList[modaList.index(myList[i])] += 1
        myList.pop() # обрезаем исходный список...для экономии памяти, в конце он пустой и он будет первым слагаемым

print(f'Уникальные значения исходного списка     - {modaList}') # Второе слагаемое
print(f'Количество вхождений уникальных значений - {countModaList}') # Третье слагаемое
print(f'Исходный список (для проверки)           - {myList}')

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
print(f'\nПодитог = {sizeCount if sizeCount < 1024 else round(sizeCount / 1024, 2)}' + ('KB' if sizeCount > 1024 else 'B'))

print('Второе слагаемое (Bites):    ', end='')
sizeCounter(modaList)
print(f'\nПодитог = {sizeCount if sizeCount < 1024 else round(sizeCount / 1024, 2)}' + ('KB' if sizeCount > 1024 else 'B'))

print('Третье слагаемое (Bites):    ', end='')
sizeCounter(countModaList)
print(f'\nПодитог = {sizeCount if sizeCount < 1024 else round(sizeCount / 1024, 2)}' + ('KB' if sizeCount > 1024 else 'B'))

print('Четвёртое слагаемое (Bites): ', end='')
sizeCounter(maxCount)
print(f'\nПодитог = {sizeCount if sizeCount < 1024 else round(sizeCount / 1024, 2)}' + ('KB' if sizeCount > 1024 else 'B'))

print('Пятое слагаемое (Bites):     ', end='')
sizeCounter(maxCount)
print(f'\n\nВсего задействовано памяти = {sizeCount if sizeCount < 1024 else round(sizeCount / 1024, 2)}' + 'KB' if sizeCount > 1024 else 'B')

# Вывод вида -  3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)] win32
#               Исходный список                          - [1, -6, 5, 7, 2, -9, -7, -5, -6, 4, -5, 3]
#               Уникальные значения исходного списка     - [3, -5, 4, -6, -7, -9, 2, 7, 5, 1]
#               Количество вхождений уникальных значений - [1, 2, 1, 2, 1, 1, 1, 1, 1, 1]
#               Исходный список (для проверки)           - []
#               Список самых "популярных" значений       -  -5  -6
#
#               Первое слагаемое (Bites):    64
#               Подитог = 64B
#               Второе слагаемое (Bites):    192 28 28 28 28 28 28 28 28 28 28
#               Подитог = 536B
#               Третье слагаемое (Bites):    192 28 28 28 28 28 28 28 28 28 28
#               Подитог = 1008B
#               Четвёртое слагаемое (Bites): 28
#               Подитог = 1.01KB
#               Пятое слагаемое (Bites):     28
#
#               Всего задействовано памяти = 1.04KB
#
#               Process finished with exit code 0
