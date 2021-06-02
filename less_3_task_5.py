# Задание 5
# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.


import random

SIZE = 20
MIN_ITEM = -50
MAX_ITEM = 50
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Начальный массив - {array}')

# 1 вариант где max_neg_num == 0
max_neg_num = 0
for i in array:
    if i < 0 and max_neg_num == 0 or 0 > i > max_neg_num:
        max_neg_num = i

print(max_neg_num)


