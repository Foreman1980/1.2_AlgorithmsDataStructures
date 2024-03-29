#     Задание № 2 урока № 2:
#     Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, в нем 3
# четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
#
#     Примечания:
#     В заданиях 2, 3, 4, 7, 8, 9 пользователь вводит только натуральные числа.
#     Попытайтесь решить задания без использования массивов в любых вариациях (массивы будут рассмотрены на следующем
# уроке). Для простоты понимания любые квадратные скобки [ и ] считаются массивами и их наличие в коде расценивается
# как неверное решение.

evenNum = 0
unevenNum = 0
num = int(input('Введите натуральное число: '))
while num != 0:
    if num % 10 % 2 == 0:
        evenNum += 1
    else:
        unevenNum += 1
    num //= 10
print(f'Введённое число состоит их {evenNum} чётных цифр и {unevenNum} нечётных.')

# Вывод вида -  Введите натуральное число: 6543135
#               Введённое число состоит их 2 чётных цифр и 5 нечётных.
#
#               Process finished with exit code 0