# https://drive.google.com/file/d/1vSSkmxbm9YG_uyA3_KVsR2geLVS68ixL/view?usp=sharing
# Задача 3.
# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.


def recursion(num):
    if len(str(num)) == 1:  # Базовый случай
        return num
    else:
        return f'{num % 10}{recursion(num // 10)}'


num = int(input('Введите натуральное число: '))

result = recursion(num)
print(int(result))

