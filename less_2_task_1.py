# https://drive.google.com/file/d/1vSSkmxbm9YG_uyA3_KVsR2geLVS68ixL/view?usp=sharing
# Задача 1.
# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не завершается, а запрашивает новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# программа должна сообщать об ошибке и снова запрашивать знак операции.
# Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.


while True:
    c = input('Введите знак операции, чтобы произвести вычисления: \nДля выхода введите 0. ')

    if c == '0':
        print("Конец")
        break
    if c == '-' or c == '+' or c == '*' or c == '/':
        a = int(input('Введите первое целое число: '))
        b = int(input('Введите второе целое число: '))
        if c == '+':
            result = a + b
            print(f'Сумма двух чисел - {result}')
        if c == '-':
            result = a - b
            print(f'Разность двух чисел - {result}')
        if c == '*':
            result = a * b
            print(f'Произведение двух чисел - {result}')
        if c == '/':
            if b == 0:
                print('Делить на 0 нельзя.')
                continue
            result = a / b
            print(f'Частное двух чисел - {result}')
    else:
        print('Вы ввели неверный знак.\n -, +, *, / или 0 для выхода. ')
        continue
