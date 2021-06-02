# https://drive.google.com/file/d/1vSSkmxbm9YG_uyA3_KVsR2geLVS68ixL/view?usp=sharing
# Задача 4.
# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.


def recursion(n, a):
    if n == 1:
        return a
    else:
        return a + recursion(n-1, a * (-0.5))

n = int(input('Введите количество элементов: '))
a = 1

result = recursion(n, a)
print(round(result, 3))



# второй вариант
# переменная a - аргумент по умолчанию
def recursion(n, a=1):
    if n == 1:
        return a
    else:
        return a + recursion(n-1, a * (-0.5))

n = int(input('Введите количество элементов: '))

result = recursion(n)
print(round(result, 3))
