# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

# Выделяемая память - 96 байт

# Вывод: больше всего затраченно памяти было в программной реализации с циклом for(556 байт).
# Реализация с рекурсией затратила меньше всего памяти(80 байт)


from sys import getsizeof


def func_sum_bytes(variables):
    sum_bytes = 0
    for i in variables:
        sum_bytes += getsizeof(i)
    return sum_bytes


n = 10
a = 1
result = 0
END = 0
while n != END:
    result += a
    a = a * (-0.5)
    n -= 1

variables = [n, a, result, END]
b = func_sum_bytes(variables)
print(f'Количество выделяемой памяти - {b} байт')
print(result)
