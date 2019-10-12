from collections import deque

HexNumList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


def simpleSum(x, y):
    z = HexNumList.index(x) + HexNumList.index(y)
    return [HexNumList[z // 16], HexNumList[z % 16]]


def simpleMult(x, y):
    z = HexNumList.index(x) * HexNumList.index(y)
    return [HexNumList[z // 16], HexNumList[z % 16]]


def hexSum(xList, yList):
    print('Проверка по разрядам:')
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
        print(f'Суммирование {digit + 1}-го разряда: {xHex} + {yHex} = {simpleSum(xHex, yHex)}')
        inMind = resultHex.pop()
        if inMind == '0':
            resultHex.extend(simpleSum(xHex, yHex)[::-1])
        else:
            spam = simpleSum(xHex, yHex)
            resultHex.extend(simpleSum(inMind, spam[1])[::-1])
            if spam[0] != 0:
                resultHex[digit + 1] = spam[0]
        digit += 1
        print(f'Накопленным итогом:                {list(resultHex)[::-1]}')
    if resultHex[digit] == '0':
        resultHex.pop()
    resultHex.reverse()
    return list(resultHex)

def hexMult(xList, yList):
    print('Проверка по разрядам:')
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
        print(f'Перемножение {digit + 1}-го разряда: {xHex} * {yHex} = {simpleMult(xHex, yHex)}')
        inMind = resultHex.pop()
        if inMind == '0':
            resultHex.extend(simpleMult(xHex, yHex)[::-1])
        else:
            spam = simpleMult(xHex, yHex)
            resultHex.extend(simpleSum(inMind, spam[1])[::-1])
            if spam[0] != 0:
                resultHex[digit + 1] = spam[0]
        digit += 1
        print(f'Накопленным итогом:                {list(resultHex)[::-1]}')
    if resultHex[digit] == '0':
        resultHex.pop()
    resultHex.reverse()
    return list(resultHex)

a = ['C', '9', 'F']
b = ['F', 'A', '3']
print(f'\nСумма чисел: {a} + {b} = {hexSum(a, b)}')

print()

a = ['1', '6', '6']
b = ['2', '7', '3']
print(f'\nПроизведение чисел: {a} * {b} = {hexMult(a, b)}')

# Вывод вида -  Проверка по разрядам:
#               Суммирование 1-го разряда: F + 3 = ['1', '2']
#               Накопленным итогом:                ['1', '2']
#               Суммирование 2-го разряда: 9 + A = ['1', '3']
#               Накопленным итогом:                ['1', '4', '2']
#               Суммирование 3-го разряда: C + F = ['1', 'B']
#               Накопленным итогом:                ['1', 'C', '4', '2']
#
#               Сумма чисел: ['C', '9', 'F'] + ['F', 'A', '3'] = ['1', 'C', '4', '2']
#
#               Проверка по разрядам:
#               Перемножение 1-го разряда: 6 * 3 = ['1', '2']
#               Накопленным итогом:                ['1', '2']
#               Перемножение 2-го разряда: 6 * 7 = ['2', 'A']
#               Накопленным итогом:                ['2', 'B', '2']
#               Перемножение 3-го разряда: 1 * 2 = ['0', '2']
#               Накопленным итогом:                ['0', '4', 'B', '2']
#
#               Произведение чисел: ['1', '6', '6'] * ['2', '7', '3'] = ['4', 'B', '2']
#
#               Process finished with exit code 0