# Задание 3
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.


import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
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

ind_min_el = array.index(min_el)
ind_max_el = array.index(max_el)

array[ind_min_el], array[ind_max_el] = array[ind_max_el], array[ind_min_el]
print(array)
