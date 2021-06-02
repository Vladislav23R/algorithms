# Задание 6
# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.


import random

SIZE = 20
MAX_ITEM = 50
MIN_ITEM = -50

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_el = array[0]
max_el = array[0]

for i in range(len(array)):
    if array[i] > max_el:
        max_el = array[i]
    if array[i] < min_el:
        min_el = array[i]

print(f'{min_el = }, {max_el = }')
a = array.index(min_el)  # индекс минимального значения в массиве
b = array.index(max_el)  # индекс максимального значения в массиве

if a > b:  # меняем местами индексы, если индекс мин значения больше индекса макс значания массива
    c = a
    a = b
    b = c

result = 0
for index, el in enumerate(array):
    if a < index < b:
        result += el

print(f'Сумма элементов между макс и мин значением массива - {result}')
