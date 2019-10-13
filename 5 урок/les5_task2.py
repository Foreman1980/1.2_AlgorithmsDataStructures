from collections import deque

HexNumList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


def simpleSum(x, y):
    z = HexNumList.index(x.upper()) + HexNumList.index(y.upper())
    return [HexNumList[z // 16], HexNumList[z % 16]]


def simpleMult(xList, y):
    z = xList[:]
    for i in range(HexNumList.index(y.upper()) - 1):
        z = hexSum(xList, z)
    return z


def hexSum(xList, yList):
    # print('Проверка по разрядам:')
    xList, yList = xList[:], yList[:]
    resultHex = deque('0')
    digit = 0
    for i in range(max(len(xList), len(yList))):
        if len(xList) > 0:
            xHex = xList.pop()
        else:
            xHex = '0'
        if len(yList) > 0:
            yHex = yList.pop()
        else:
            yHex = '0'
        # print(f'Суммирование {digit + 1}-го разряда: {xHex} + {yHex} = {simpleSum(xHex, yHex)}')
        inMind = resultHex.pop()
        if inMind == '0':
            resultHex.extend(simpleSum(xHex, yHex)[::-1])
        else:
            spam = simpleSum(xHex, yHex)
            resultHex.extend(simpleSum(inMind, spam[1])[::-1])
            if spam[0] != 0:
                resultHex[digit + 1] = spam[0]
        digit += 1
        # print(f'Накопленным итогом:                {list(resultHex)[::-1]}')
    if resultHex[digit] == '0':
        resultHex.pop()
    resultHex.reverse()
    return list(resultHex)

def hexMult(xList, yList):
    if len(yList) > len(xList):
        xList, yList = yList[:], xList[:]
    else:
        xList, yList = xList[:], yList[:]
    resultHex = deque()
    digit = 0
    spam = ['0']
    # print(f'Перемножение по разрядам числа {yList}:')
    for i in yList[::-1]:
        resultHex.clear()
        resultHex.extend(simpleMult(xList, i))
        if resultHex[0] == '0':
            resultHex.popleft()
        resultHex.extend(['0' for _ in range(digit)])
        # print(f'Действие № {digit + 1}: {xList} * {yList[len(yList) - digit - 1]} = {list(resultHex)}')
        spam = hexSum(spam, list(resultHex))
        # print(f'Накопленным итогом:                 {spam}')
        digit += 1
    return spam

a = ['a', '2']
b = ['c', '4', 'F']
print(f'\nСумма чисел: {a} + {b} = {hexSum(a, b)}')
print(f'\nПроизведение чисел: {a} * {b} = {hexMult(a, b)}')

# Вывод вида - Сумма чисел: ['a', '2'] + ['c', '4', 'F'] = ['C', 'F', '1']
#
#               Произведение чисел: ['a', '2'] * ['c', '4', 'F'] = ['7', 'C', '9', 'F', 'E']
#
#               Process finished with exit code 0
#
########################################################################################################################
#               Если раскомментровать принты ОТДЕЛЬНО для сложения и для умножения, то можно проверить счёт в "столбик"
#               (нужно учитывать, что сложение используется при перемножении, т.е. лог для умножения резко увеличиться):
########################################################################################################################
#
#               Проверка по разрядам:
#               Суммирование 1-го разряда: 2 + F = ['1', '1']
#               Накопленным итогом:                ['1', '1']
#               Суммирование 2-го разряда: a + 4 = ['0', 'E']
#               Накопленным итогом:                ['0', 'F', '1']
#               Суммирование 3-го разряда: 0 + c = ['0', 'C']
#               Накопленным итогом:                ['0', 'C', 'F', '1']
#
#               Сумма чисел: ['a', '2'] + ['c', '4', 'F'] = ['C', 'F', '1']
#
#               Перемножение по разрядам числа ['a', '2']:
#               Действие № 1: ['c', '4', 'F'] * 2 = ['1', '8', '9', 'E']
#               Накопленным итогом:                 ['1', '8', '9', 'E']
#               Действие № 2: ['c', '4', 'F'] * a = ['7', 'B', '1', '6', '0']
#               Накопленным итогом:                 ['7', 'C', '9', 'F', 'E']
#
#               Произведение чисел: ['a', '2'] * ['c', '4', 'F'] = ['7', 'C', '9', 'F', 'E']
#
#               Process finished with exit code 0