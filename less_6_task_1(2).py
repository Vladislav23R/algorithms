# Задание 1.
# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.


# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

# Выделяемая память - 556 байт
# ОС(Windows) 64bit, Python 3.8.6 64bit

from sys import getsizeof


def func_sum_bytes(variables):
    sum_bytes = 0
    for variable in variables:
        if isinstance(variable, list):
            for item in variable:
                sum_bytes += getsizeof(item)
        sum_bytes += getsizeof(variable)
    return sum_bytes


n = 10
a = 1
result = 0
b = []
for i in range(n):
    b.append(a)
    a *= (-0.5)
    if i == n - 1:
        for j in b:
            result += j


variables = [n, a, result, b, i, j]

c = func_sum_bytes(variables)
print(f'Количество выделяемой памяти - {c} байт')
print(result)
