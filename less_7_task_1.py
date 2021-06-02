# Задание 1
# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.


from random import randint


def bubble_sort(arr):
    array = arr
    n = 1
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
    return array


SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print('Изначальный массив: ', *array, '\n')

result = bubble_sort(array)
print('Отсортированный массив: ', *result)
