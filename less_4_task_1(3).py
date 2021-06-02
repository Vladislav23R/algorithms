# Задача 4.
# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.
# Третий вариант


import timeit
import cProfile


def sum(n):
    a = 1
    result = 0
    b = []
    for i in range(n):
        b.append(a)
        a *= (-0.5)
        if i == n - 1:
            for j in b:
                result += j


n = 100

print(timeit.timeit('sum(n)', number=1_000, globals=globals()))  # 0.034575588000000004
print(timeit.timeit('sum(n * 2)', number=1_000, globals=globals()))  # 0.075451812
print(timeit.timeit('sum(n * 4)', number=1_000, globals=globals()))  # 0.15431316300000003
print(timeit.timeit('sum(n * 6)', number=1_000, globals=globals()))  # 0.22624938199999994
print(timeit.timeit('sum(n * 8)', number=1_000, globals=globals()))  # 0.314689353

# cProfile.run('sum(n)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 less_4_task_1(3).py:10(sum)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#    100    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# cProfile.run('sum(n * 200)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.015    0.015 <string>:1(<module>)
#      1    0.012    0.012    0.015    0.015 less_4_task_1(3).py:10(sum)
#      1    0.000    0.000    0.015    0.015 {built-in method builtins.exec}
#  20000    0.003    0.000    0.003    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# cProfile.run('sum(n * 400)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.020    0.020 <string>:1(<module>)
#      1    0.015    0.015    0.019    0.019 less_4_task_1(3).py:10(sum)
#      1    0.000    0.000    0.020    0.020 {built-in method builtins.exec}
#  40000    0.004    0.000    0.004    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# cProfile.run('sum(n * 600)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.001    0.001    0.027    0.027 <string>:1(<module>)
#      1    0.021    0.021    0.026    0.026 less_4_task_1(3).py:10(sum)
#      1    0.000    0.000    0.027    0.027 {built-in method builtins.exec}
#  60000    0.006    0.000    0.006    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# cProfile.run('sum(n * 800)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.001    0.001    0.035    0.035 <string>:1(<module>)
#      1    0.027    0.027    0.033    0.033 less_4_task_1(3).py:10(sum)
#      1    0.000    0.000    0.035    0.035 {built-in method builtins.exec}
#  80000    0.006    0.000    0.006    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
