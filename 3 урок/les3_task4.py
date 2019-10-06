#     Задание № 4 урока № 3:
#     Определить, какое число в массиве встречается чаще всего.
#
#     Примечания:
#     Попытайтесь решить задания без использования функций max, min, sum, sorted и их аналогов, в том числе написанных
# самостоятельно.

from random import randint

myList = [randint(-10, 10) for _ in range(randint(10, 20))]
print(f'Исходный список                          - {myList}')
print(f'Уникальные значения исходного списка     - {set(myList)}')

# Создание словаря из множества и списка, как показано в конце первого видео - не работает...расходимся нас обманули)
# modaDict = {frozenset(myList): [0 for _ in range(len(set(myList)))]}
# print(modaDict)
# Вывод вида -  [1, -6, 5, 7, 2, -9, -7, -5, -6, 4, -5, 3]
#               {frozenset({1, 2, 3, 4, 5, 7, -9, -7, -6, -5}): [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}

# Придётся делать в цикле:
modaDict = {}
for i in set(myList):
    modaDict.update({i: 0})
print(f'Словарь с ключами из уникальных значений - {modaDict}')

for item in myList:
    modaDict[item] += 1
print(f'Подсчитано количество вхождений значений - {modaDict}')

maxCount = 0
for value in modaDict.values():
    if value > maxCount:
        maxCount = value

resultList = []
for key in modaDict.keys():
    if modaDict[key] == maxCount:
        resultList.append(key)
print(f'Список самых "популярных" значений       - {resultList}')

# Вывод вида -  Исходный список                          - [1, -6, 5, 7, 2, -9, -7, -5, -6, 4, -5, 3]
#               Уникальные значения исходного списка     - {1, 2, 3, 4, 5, 7, -9, -7, -6, -5}
#               Словарь с ключами из уникальных значений - {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 7: 0, -9: 0, -7: 0, -6: 0, -5: 0}
#               Подсчитано количество вхождений значений - {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 7: 1, -9: 1, -7: 1, -6: 2, -5: 2}
#               Список самых "популярных" значений       - [-6, -5]
#
#               Process finished with exit code 0
