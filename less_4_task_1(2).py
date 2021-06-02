# Задача 4.
# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.
# Второй вариант

import timeit
import cProfile


def sum(n):
    a = 1
    result = 0
    while n != 0:
        result += a
        a = a * (-0.5)
        n -= 1

n = 100


print(timeit.timeit('sum(n)', number=1_000, globals=globals()))  # 0.019517012
print(timeit.timeit('sum(n * 2)', number=1_000, globals=globals()))  # 0.039655719
print(timeit.timeit('sum(n * 4)', number=1_000, globals=globals()))  # 0.081290352
print(timeit.timeit('sum(n * 6)', number=1_000, globals=globals()))  # 0.09365180100000003
print(timeit.timeit('sum(n * 8)', number=1_000, globals=globals()))  # 0.09566523599999999


cProfile.run('sum(n)')
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
   #      1    0.000    0.000    0.000    0.000 test.py:9(sum)
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('sum(n * 200)')
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.004    0.004 <string>:1(<module>)
   #      1    0.004    0.004    0.004    0.004 test.py:9(sum)
   #      1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('sum(n * 400)')
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.010    0.010 <string>:1(<module>)
   #      1    0.010    0.010    0.010    0.010 test.py:9(sum)
   #      1    0.000    0.000    0.010    0.010 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('sum(n * 600)')
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.013    0.013 <string>:1(<module>)
   #      1    0.013    0.013    0.013    0.013 test.py:9(sum)
   #      1    0.000    0.000    0.013    0.013 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('sum(n * 800)')
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.020    0.020 <string>:1(<module>)
   #      1    0.020    0.020    0.020    0.020 test.py:9(sum)
   #      1    0.000    0.000    0.020    0.020 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
