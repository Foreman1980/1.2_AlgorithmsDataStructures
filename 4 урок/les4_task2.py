import math

def classicSieve(n):
    simpleNumList = [2]
    checkNum = simpleNumList[-1]
    while len(simpleNumList) < n:
        checkNum += 1
        for i in range(2, int(math.sqrt(checkNum)) + 1):
            if checkNum % i == 0:
                break
        else:
            simpleNumList.append(checkNum)
            checkNum = simpleNumList[-1] + 1
    else:
        return simpleNumList[-1]

def eratosSieve(n):
    numList = [i for i in range(int(n * n))] # в этой строке вся проблема
    numList[1] = 0
    simpleNumList = []
    ind = 2
    while len(simpleNumList) < n:
        if numList[ind] != 0:
            simpleNumList.append(ind)
            for i in range(ind * 2, len(numList), ind):
                numList[i] = 0
        if ind < len(numList):
            ind += 1
    else:
        return simpleNumList[-1]

# проверка
n = 20
print(classicSieve(n), eratosSieve(n))

# сделать то сделал, но не понятно за какие уши притянуть под условие алгоритм на базе "решета Эратосфена"...элементарно
# понятно при поиске простых чисел до указанного числа N, но чтобы его использовать под данное условие, нужно заранее
# знать сколько чисел нужно анализировать (см. строку 18)...я задолбался) времени нет тупить несколько дней, селяви





