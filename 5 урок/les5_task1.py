#     Задание № 1 урока № 5:
#     Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
# предприятий, чья прибыль выше среднего и ниже среднего.

from collections import deque
from collections import OrderedDict
from random import random, randint

companyNames = deque()
companyProfits = deque()

# чтобы не вводить данные с клавиатуры:
companyNames = [f'comp{_ + 1}' for _ in range(randint(3, 15))]
companyProfits = [round(random() * 1000, 2) for _ in range(len(companyNames))]

# for i in range(int(input('Введите количество предприятий: '))):
#     companyName, companyProfit = input(f'Введите наименование предприятия № {i + 1} и его годовую прибыль (млн р) (через пробел): ').split()
#     companyNames.append(companyName)
#     companyProfits.append(round(float(companyProfit), 2))

print(companyNames)
print(companyProfits)
averageProfit = sum(companyProfits) / len(companyProfits)

print(f'Средняя годовая прибыль по отрасли = {round(averageProfit, 2)}')

print('-' * 100)
enterprises = OrderedDict(sorted(dict(zip(companyNames, companyProfits)).items(), key=lambda _: _[1], reverse=True))
print(enterprises)
print('-' * 100)

print('Список предприятий с годовой прибылью выше средней:\n    ', end='')
check = True
for key, item in enterprises.items():
    if item < averageProfit and check == True:
        print('\nСписок предприятий с годовой прибылью ниже средней:\n    ', end='')
        check = False
    print(key, end=' ')

# Вывод вида -  ['comp1', 'comp2', 'comp3', 'comp4', 'comp5']
#               [23.83, 308.61, 244.0, 597.99, 212.51]
#               Средняя годовая прибыль по отрасли = 277.39
#               ----------------------------------------------------------------------------------------------------
#               OrderedDict([('comp4', 597.99), ('comp2', 308.61), ('comp3', 244.0), ('comp5', 212.51), ('comp1', 23.83)])
#               ----------------------------------------------------------------------------------------------------
#               Список предприятий с годовой прибылью выше средней:
#                   comp4 comp2
#               Список предприятий с годовой прибылью ниже средней:
#                   comp3 comp5 comp1
#               Process finished with exit code 0
