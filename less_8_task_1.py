# Задание 1
# Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
#
# func("papa")
# 6
# func("sova")
# 9

import hashlib


def func(value):
    list_hash = []
    for index, char in enumerate(value):
        egg = char
        if hashlib.sha256(value[index].encode('utf-8')).hexdigest() not in list_hash:
            list_hash.append(hashlib.sha256(value[index].encode('utf-8')).hexdigest())
        for j in value[index + 1:]:
            egg += j
            if hashlib.sha256(str(egg).encode('utf-8')).hexdigest() not in list_hash and egg != value:
                list_hash.append(hashlib.sha256(str(egg).encode('utf-8')).hexdigest())
    return len(list_hash)


result = func('sova')
print(result)
