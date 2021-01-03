# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

# Выделяемая память - 80 байт

from sys import getsizeof


def recursion(n, a):
    if n == 1:
        return a
    else:
        return a + recursion(n - 1, a * (-0.5))

def func_sum_bytes(variables):
    sum_bytes = 0
    for i in variables:
        sum_bytes += getsizeof(i)
    return sum_bytes

n = 10
a = 1

result = recursion(n, a)

variables = [n, a, result]

b = func_sum_bytes(variables)
print(f'Количество выделяемой памяти - {b} байт')
print(result)
