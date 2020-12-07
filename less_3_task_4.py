# Задание 4
# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 50
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Начальный массив - {array}\n')

dict_el = {}

for i in array:
    if i in dict_el.keys():
        dict_el[i] = dict_el[i] + 1
    else:
        dict_el[i] = 1

print(f'Словарь с количеством повторяющихся элементов массива:\n {dict_el}\n')

max_el_count = 0

for key, item in dict_el.items():
    if max_el_count == 0 or item > max_el_count:
        max_el_count = item

print(f'Максимальное количество повторов числа - {max_el_count}\n')

result = [str(i) for i in dict_el if dict_el[i] == max_el_count]

print(f"Цисло(а), которое(ые) встречается(ются) больше всего - {', '.join(result)}")
