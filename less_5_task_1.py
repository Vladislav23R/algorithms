# Задание 1
# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.


from collections import namedtuple

Firma = namedtuple('Firma', 'name_firm, quarter_1, quarter_2, quarter_3, quarter_4')
count_companies = int(input('Введите количество компаний: '))

companies = []

for i in range(1, count_companies + 1):  # создаем  объекты с названием компании и  ее прибылью
    name = input('введите название фирмы: ')
    firm_i = Firma(
        name,
        input('Введите прибыль за первый квартал: '),
        input('Введите прибыль за второй квартал: '),
        input('Введите прибыль за третий квартал: '),
        input('Введите прибыль за четвертый квартал: ')
    )
    companies.append(firm_i)

average_profit = 0
company_year_profit = {}
for i in companies:  # считаем среднюю годовую прибыль всех компаний и годовую прибыль каждой компании
    profit_year = 0
    for j in i:
        if j.isnumeric():
            profit_year += float(j)
    company_year_profit[i.name_firm] = profit_year
    average_profit += profit_year

average_profit /= count_companies


above_average = [key for key, value in company_year_profit.items() if value > average_profit]
less_than_average = [key for key, value in company_year_profit.items() if value < average_profit]

print(f'Компании чья прибыль больше средней прибыли всех компаний - {",".join(above_average)}'
      if len(above_average) > 0 else 'Нет компаний прибыль которых выше средней прибыли всех компаний')
print(f'Компании чья прибыль меньше средней прибыли всех компаний - {",".join(less_than_average)}'
      if len(less_than_average) > 0 else 'Нет компаний прибыль которых ниже средней прибыли всех компаний')
