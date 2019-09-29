#     Задание № 1 урока № 2:
#     Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не завершается, а запрашивает новые данные для вычислений. Завершение программы должно выполняться
# при вводе символа '0' в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), программа должна
# сообщать об ошибке и снова запрашивать знак операции. Также она должна сообщать пользователю о невозможности деления на ноль, если он
# ввел его в качестве делителя.
#
#     Примечания:
#     Попытайтесь решить задания без использования массивов в любых вариациях (массивы будут рассмотрены на следующем уроке). Для простоты
# понимания любые квадратные скобки [ и ] считаются массивами и их наличие в коде расценивается как неверное решение.

oper = None
while True:
    oper = input("Введите символ операции ('+', '-', '*', '/') или '0' для выхода: ")
    if oper == '0':
        break
    elif oper == '+':
        a = 'первое слагаемое'
        b = 'второе слагаемое'
        c = 'Сумма'
    elif oper == '-':
        a = 'уменьшаемое'
        b = 'вычитаемое'
        c = 'Разница'
    elif oper == '*':
        a = 'первый множитель'
        b = 'второй множитель'
        c = 'Произведение'
    elif oper == '/':
        a = 'делимое'
        b = 'делитель'
        c = 'Частное'
    else:
        print('Ошибка, повторите ввод символа операции: ')
    x = int(input(f'Ведите {a} - '))
    y = int(input(f'Ведите {b} - '))
    while oper == '/' and y == 0:
        print('Ошибка, деление на ноль!')
        y = int(input(f'Ведите {b} - '))
    if oper == '+':
        print(f'{c} - ', x + y)
    elif oper == '-':
        print(f'{c} - ', x - y)
    elif oper == '*':
        print(f'{c} - ', x * y)
    else:
        print(f'{c} - ', x / y)

# Вывод вида -  Введите символ операции ('+', '-', '*', '/') или '0' для выхода: : +
#               Ведите первое слагаемое - 1
#               Ведите второе слагаемое - 2
#               Сумма -  3
#               Введите символ операции ('+', '-', '*', '/') или '0' для выхода: : -
#               Ведите уменьшаемое - 2
#               Ведите выситаемое - 1
#               Разница -  1
#               Введите символ операции ('+', '-', '*', '/') или '0' для выхода: : *
#               Ведите первый множитель - 2
#               Ведите второй множитель - 3
#               Произведение -  6
#               Введите символ операции ('+', '-', '*', '/') или '0' для выхода: : /
#               Ведите делимое - 4
#               Ведите делитель - 2
#               Частное -  2.0
#               Введите символ операции ('+', '-', '*', '/') или '0' для выхода: : 0
#
#               Process finished with exit code 0