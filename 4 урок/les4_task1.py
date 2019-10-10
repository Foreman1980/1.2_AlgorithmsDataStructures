from random import randint
import cProfile

def minimax(n, var):
    # намеренно не оптимальный вариант - перебираем матрицу по строкам, мин. значение элементов столбцов сохраняем
    # в списке, в котором потом ищем максимальный элемент
    def _minimax1(n):
        myMatrix = [[randint(-100, 100) for i in range(n)] for j in range(n)]
        listOfMin = [float('+inf')] * n
        for i in range(n):
            for j in range(n):
                if myMatrix[i][j] < listOfMin[j]:
                    listOfMin[j] = myMatrix[i][j]
        result = listOfMin[0]
        for i in listOfMin:
            if i > result:
                result = i
        return result

    def _minimax2(n):
        # вариант, в которым перебор идёт по столбцам матрицы и для хранения минимальных значений элементов столбцов
        # матрицы используется переменная, а не список
        myMatrix = [[randint(-100, 100) for i in range(n)] for j in range(n)]
        maxItem = float('-inf')
        for i in range(n):
            minItem = myMatrix[0][i]
            for j in range(1, n):
                if myMatrix[j][i] < minItem:
                    minItem = myMatrix[j][i]
            if minItem > maxItem:
                maxItem = minItem
        return maxItem

    def _minimax3(n):
        # вариант, в которым мы используем не матрицу, а одномерный список и условную принадлежеость элемента столбцу
        # определяем по остатку от деления его индекса на размерность матрицы по условию
        # myMatrixList = []
        # for row in myMatrix:
        #     myMatrixList += row
        myMatrixList = [randint(-100, 100) for i in range(n * n)]
        listOfMin = myMatrixList[:n]
        for i, item in enumerate(myMatrixList):
            if item < listOfMin[i % n]:
                listOfMin[i % n] = item
        result = listOfMin[0]
        for i in listOfMin:
            if i > result:
                result = i
        return result

    if var == 1:
        return _minimax1(n)
    elif var == 2:
        return _minimax2(n)
    else:
        return _minimax3(n)

# n = 10
# myMatrix = [[randint(-100, 100) for i in range(n)] for j in range(n)]
# print(minimax(myMatrix, 1), minimax(myMatrix, 2), minimax(myMatrix, 3))
# проверка показала одинаковый результат работы функций, но для избежания лишней операции в третьей функции по
# "распремлению" матрицы, данные желательно формировать у них внутри (результат нас уже не интересует, интересует
# скорость выполнения)

# n = 10
# print(minimax(n, 1), minimax(n, 2), minimax(n, 3))
# ещё одна проверка, теперь подаём на вход только размерность данных и вариант решения для оценки...всё работает, можно
# переходить в терминал

# python -m timeit -n 1000 -s "import les4_task1" "les4_task1.minimax(10, 1)"

# см. сравненние ниже

# "les4_task1.minimax(10, 1/2/3)"
# 1000 loops, best of 5: 103 usec per loop/
# 1000 loops, best of 5: 92.2 usec per loop/
# 1000 loops, best of 5: 95.1 usec per loop

# "les4_task1.minimax(20, 1/2/3)"
# 1000 loops, best of 5: 375 usec per loop/
# 1000 loops, best of 5: 396 usec per loop/
# 1000 loops, best of 5: 392 usec per loop

# "les4_task1.minimax(50, 1/2/3)"
# 1000 loops, best of 5: 2.47 msec per loop/
# 1000 loops, best of 5: 2.3 msec per loop/
# 1000 loops, best of 5: 2.43 msec per loop

# "les4_task1.minimax(100, 1/2/3)"
# 1000 loops, best of 5: 9.55 msec per loop/
# 1000 loops, best of 5: 9.41 msec per loop/
# 1000 loops, best of 5: 9.35 msec per loop

# "les4_task1.minimax(200, 1/2/3)"
# 1000 loops, best of 5: 38.5 msec per loop/
# 1000 loops, best of 5: 37.8 msec per loop/
# 1000 loops, best of 5: 34.4 msec per loop

# cProfile.run('minimax(10, 1/2/3)')
# 531 function calls in 0.000 seconds / 536 function calls in 0.000 seconds / 530 function calls in 0.000 seconds
# cProfile.run('minimax(20, 1/2/3)')
# 2125 function calls in 0.001 seconds / 2118 function calls in 0.001 seconds / 2102 function calls in 0.001 seconds
# cProfile.run('minimax(50, 1/2/3)')
# 13131 function calls in 0.003 seconds / 13222 function calls in 0.003 seconds / 13220 function calls in 0.005 seconds
# cProfile.run('minimax(100, 1/2/3)')
# 52741 function calls in 0.012 seconds / 52745 function calls in 0.012 seconds / 52752 function calls in 0.014 seconds
# cProfile.run('minimax(200, 1/2/3)')
# 211055 function calls in 0.053 seconds / 211039 function calls in 0.050 seconds / 210670 function calls in 0.057 seconds
# cProfile.run('minimax(10000, 1/2/3)')
# 527364128 function calls in 127.931 seconds/
# 527356280 function calls in 130.385 seconds/
# 527369611 function calls in 141.182 seconds

# В общем разницы нет...