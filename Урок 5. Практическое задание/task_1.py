"""
Задание 1.

Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените коллекцию из модуля collections
Для лучшего освоения материала можете сделать
несколько варианто решения этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога
Предприятия, с прибылью ниже среднего значения: Копыта
"""
from collections import defaultdict


def try_value(in_str):
    try:
        return int(in_str)
    except ValueError:
        try:
            return round(float(in_str), 2)
        except ValueError:
            exit('Введены неправильные данные')


try:
    count = int(input('Введите количество предприятий для расчета прибыли: '))
except ValueError:
    exit('Введены неправильные данные')
avg = 0
result = defaultdict(list)
firms = {}
for i in range(count):
    name = input('Введите название предприятия: ')
    profit = input(
        'через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ').split(' ', 4)
    profit = [try_value(el) for el in profit]
    avg += sum(profit)
    firms[name] = profit
avg = round(avg/count)
print('Средняя годовая прибыль всех предприятий: ', avg)
for k, v in firms.items():
    if sum(v) >= avg:
        result['up'].append(k)
    else:
        result['low'].append(k)
print(f'Предприятия, с прибылью выше среднего значения: {"".join(f"{el} " for el in result["up"])}')
print(f'Предприятия, с прибылью ниже среднего значения: {"".join(f"{el} " for el in result["low"])}')
