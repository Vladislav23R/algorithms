# https://drive.google.com/file/d/1vSSkmxbm9YG_uyA3_KVsR2geLVS68ixL/view?usp=sharing
# Задача 8.
# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

n = int(input('Введите количество чисел: '))
num = int(input('Введите цифру для поиска в последовательности: '))

count = 0  # Кол-во вхождений в последовательность чисел

while n != 0:
    a = input('Введите натуральное число: ')
    n -= 1
    for i in a:
        if int(i) == num:
            count += 1
        else:
            continue

print(f'Число {num} входит в последовательность чисел {count} раз(а).')
