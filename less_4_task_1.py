# Задача 4.
# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.
# Первый вариант

import timeit
import cProfile

def recursion(n, a):
    if n == 1:
        return a
    else:
        return a + recursion(n - 1, a * (-0.5))


n = 100
a = 1

# result = recursion(n, a)

print(timeit.timeit('recursion(n, a)', number=1000, globals=globals()))  # 0.022696087999999996
print(timeit.timeit('recursion(n * 2, a)', number=1000, globals=globals()))  # 0.033831561
print(timeit.timeit('recursion(n * 4, a)', number=1000, globals=globals()))  # 0.08073334599999998
print(timeit.timeit('recursion(n * 6, a)', number=1000, globals=globals()))  # 0.127830441
print(timeit.timeit('recursion(n * 8, a)', number=1000, globals=globals()))  # 0.17012751200000004

cProfile.run('recursion(n, a)')
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
   #  100/1    0.000    0.000    0.000    0.000 less_4_task_1.py:9(recursion)
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('recursion(n * 2, a)')
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
   #  200/1    0.000    0.000    0.000    0.000 less_4_task_1.py:9(recursion)
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('recursion(n * 4, a)')
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
   #  400/1    0.000    0.000    0.000    0.000 less_4_task_1.py:9(recursion)
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('recursion(n * 6, a)')
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
   #  600/1    0.000    0.000    0.000    0.000 less_4_task_1.py:9(recursion)
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('recursion(n * 8, a)')
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
   #  800/1    0.000    0.000    0.000    0.000 less_4_task_1.py:9(recursion)
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Вывод:
# Алгоритмы с рекурскией и циклом for - имеют линейный график.
# График алгоритма с циклом while - больше похож на квадритичный.
# Алгоритм с рекурсией на заданных данных показал себя быстрее остальных
