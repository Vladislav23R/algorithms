# Задание 7
# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.


import random


SIZE = 20
MIN_ITEM = -20
MAX_ITEM = 50
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_num_1 = None
min_num_2 = None

for i in array:
    if min_num_1 is None or i < min_num_1:
        min_num_1 = i

for index, el in enumerate(array):
    if el == min_num_1 and index == array.index(min_num_1):
        continue
    if el == min_num_1 and index != array.index(min_num_1):
        min_num_2 = el
        break
    if min_num_2 is None or el < min_num_2:
        min_num_2 = el

print(f'Первый мин элемент - {min_num_1}')
print(f'Второй мин элемент - {min_num_2}')
