# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

# Сделал только сложение


from collections import deque

my_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
           'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

a = deque(input('Введите первое шестнадцатеричное число: ').upper())
b = deque(input('Введите второе шестнадцатеричное число: ').upper())

result_sum = deque()

if len(a) < len(b):  # меняем местами для удобства расчетов
    a, b = b, a

a.reverse()
b.reverse()

k = 0
S_S = 16  # система счисления

for i in range(len(a) + 1):
    if i == len(a):
        if k != 0:
            result_sum.append(str(k))
        break

    if i > (len(b) - 1):
        sum_num = my_dict[a[i]] + 0
    else:
        sum_num = my_dict[a[i]] + my_dict[b[i]]

    if k != 0:
        sum_num += k
        k = 0

    if sum_num > S_S:
        k = 1
        sum_num = sum_num % S_S

    for key, value in my_dict.items():
        if sum_num == value:
            result_sum.append(key)
            break


result_sum.reverse()

print(result_sum)
