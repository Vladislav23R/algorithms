# Задание 2
# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.


from random import uniform


def merge_lists(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        elif left[i] > right[j]:
            result.append(right[j])
            j += 1

    if i < len(left):
        result += left[i:]
    if j < len(right):
        result += right[j:]

    return result


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    count = len(arr)
    right = merge_sort(arr[count // 2:])
    left = merge_sort(arr[:count // 2])

    return merge_lists(left, right)


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 50

array = [round(uniform(MIN_ITEM, MAX_ITEM), 2) for _ in range(SIZE)]
print('Изначальный массив: ', *array)

result = merge_sort(array)
print('\n''Отсортированный массив: ', *result)
