#    Задание № 1 урока № 6 вариант № 1 (как в домашке к уроку № 3):
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

#     Задание № 4 урока № 3 (вариант из домашки):
#     Определить, какое число в массиве встречается чаще всего.
#
#     Примечания:
#     Попытайтесь решить задания без использования функций max, min, sum, sorted и их аналогов, в том числе написанных
# самостоятельно.

# from random import randint

# myList = [randint(-10, 10) for _ in range(randint(10, 20))]
myList = [1, -6, 5, 7, 2, -9, -7, -5, -6, 4, -5, 3] # для повторяемости результатов задаём начальный список
print(f'Исходный список                          - {myList}') # Первое слагаемое
print(f'Уникальные значения исходного списка     - {set(myList)}') # Второе слагаемое, т.к. память же тоже занимает...

modaDict = {} # это временное значение, не считаем, т.к. словарь "modaDict" потом будет ссылаться на другую область
              # памяти и счётчик обнулиться, следовательно память очистится...наверно
for i in set(myList): # Третье слагаемое, т.к. видимо создаётся ещё одно множество в памяти
    modaDict.update({i: 0}) # "i" это четвёртое слагаемое и только последнее сохранённое значение
print(f'Словарь с ключами из уникальных значений - {modaDict}') # Пока не учитываем, т.к. позже нули заменим значениями

for item in myList:
    modaDict[item] += 1
print(f'Подсчитано количество вхождений значений - {modaDict}') # Пятое слагаемое

maxCount = 0 # это временное значение, не считаем (по вышеуказанному предположению)
for value in modaDict.values(): # "modaDict.values()" - шестое слагаемое, под него же выделилось место в памяти
    if value > maxCount:
        maxCount = value # Седьмое и восьмое слагаемые, "value" берём только последнее значение

resultList = [] # это временное значение, не считаем (по вышеуказанному предположению)
for key in modaDict.keys(): # "modaDict.keys()" - девятое слагаемое, под него же выделилось место в памяти
    if modaDict[key] == maxCount:
        resultList.append(key)
print(f'Список самых "популярных" значений       - {resultList}') # Десятое слагаемое

print('\nПервое слагаемое (Bites):    ', end='')
sizeCounter(myList)
print(f'\nПодитог = {sizeCount if sizeCount < 1024 else round(sizeCount / 1024, 2)}' + ('Kb' if sizeCount > 1024 else 'B'))

print('Второе слагаемое (Bites):    ', end='')
sizeCounter(set(myList)) # хотя я создал ещё одно множество...
print(f'\nПодитог = {sizeCount if sizeCount < 1024 else round(sizeCount / 1024, 2)}' + ('Kb' if sizeCount > 1024 else 'B'))

print('Третье слагаемое (Bites):    ', end='')
sizeCounter(set(myList)) # и ещё...
print(f'\nПодитог = {sizeCount if sizeCount < 1024 else round(sizeCount / 1024, 2)}' + ('Kb' if sizeCount > 1024 else 'B'))

print('Четвёртое слагаемое (Bites): ', end='')
sizeCounter(i)
print(f'\nПодитог = {sizeCount if sizeCount < 1024 else round(sizeCount / 1024, 2)}' + ('Kb' if sizeCount > 1024 else 'B'))

print('Пятое слагаемое (Bites):     ', end='')
sizeCounter(modaDict)
print(f'\nПодитог = {sizeCount if sizeCount < 1024 else round(sizeCount / 1024, 2)}' + ('Kb' if sizeCount > 1024 else 'B'))

print('Шестое слагаемое (Bites):    ', end='')
sizeCounter(modaDict.values())
print(f'\nПодитог = {sizeCount if sizeCount < 1024 else round(sizeCount / 1024, 2)}' + ('Kb' if sizeCount > 1024 else 'B'))

print('Седьмое слагаемое (Bites):   ', end='')
sizeCounter(maxCount)
print(f'\nПодитог = {sizeCount if sizeCount < 1024 else round(sizeCount / 1024, 2)}' + ('Kb' if sizeCount > 1024 else 'B'))

print('Восьмое слагаемое (Bites):   ', end='')
sizeCounter(value)
print(f'\nПодитог = {sizeCount if sizeCount < 1024 else round(sizeCount / 1024, 2)}' + ('Kb' if sizeCount > 1024 else 'B'))

print('Девятое слагаемое (Bites):   ', end='')
sizeCounter(modaDict.keys())
print(f'\nПодитог = {sizeCount if sizeCount < 1024 else round(sizeCount / 1024, 2)}' + ('Kb' if sizeCount > 1024 else 'B'))

print('Десятое слагаемое (Bites):   ', end='')
sizeCounter(resultList)
print(f'\n\nВсего задействовано памяти = {sizeCount if sizeCount < 1024 else round(sizeCount / 1024, 2)}' + 'KB' if sizeCount > 1024 else 'B')

# Вывод вида -  3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)] win32
#
#               Исходный список                          - [1, -6, 5, 7, 2, -9, -7, -5, -6, 4, -5, 3]
#               Уникальные значения исходного списка     - {1, 2, 3, 4, 5, 7, -9, -7, -6, -5}
#               Словарь с ключами из уникальных значений - {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 7: 0, -9: 0, -7: 0, -6: 0, -5: 0}
#               Подсчитано количество вхождений значений - {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 7: 1, -9: 1, -7: 1, -6: 2, -5: 2}
#               Список самых "популярных" значений       - [-6, -5]
#
#               Первое слагаемое (Bites):    160 28 28 28 28 28 28 28 28 28 28 28 28
#               Подитог = 496B
#               Второе слагаемое (Bites):    736 28 28 28 28 28 28 28 28 28 28
#               Подитог = 1.48KB
#               Третье слагаемое (Bites):    736 28 28 28 28 28 28 28 28 28 28
#               Подитог = 2.47KB
#               Четвёртое слагаемое (Bites): 28
#               Подитог = 2.5KB
#               Пятое слагаемое (Bites):     368 64 28 28 64 28 28 64 28 28 64 28 28 64 28 28 64 28 28 64 28 28 64 28 28 64 28 28 64 28 28
#               Подитог = 4.03KB
#               Шестое слагаемое (Bites):    48 28 28 28 28 28 28 28 28 28 28
#               Подитог = 4.35KB
#               Седьмое слагаемое (Bites):   28
#               Подитог = 4.38KB
#               Восьмое слагаемое (Bites):   28
#               Подитог = 4.4KB
#               Девятое слагаемое (Bites):   48 28 28 28 28 28 28 28 28 28 28
#               Подитог = 4.72KB
#               Десятое слагаемое (Bites):   96 28 28

#               Всего задействовано памяти = 4.87KB
#
#               Process finished with exit code 0