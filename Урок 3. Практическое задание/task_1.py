"""
Задание 1.

Реализуйте:

a) заполнение списка, оцените сложность в O-нотации.
   заполнение словаря, оцените сложность в O-нотации.
   сделайте аналитику, что заполняется быстрее и почему.
   сделайте замеры времени.

b) выполните со списком и словарем операции: изменения и удаления элемента.
   оцените сложности в O-нотации для операций
   получения и удаления по списку и словарю
   сделайте аналитику, какие операции быстрее и почему
   сделайте замеры времени.


ВНИМАНИЕ: в задании два пункта - а) и b)
НУЖНО выполнить оба пункта

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""

import random
import time


def time_of_function(function):
    def wrapped(*args):
        start_time = time.perf_counter_ns()
        for i in range(1000):
            res = function(*args)
        print(f'Функция: {function.__name__}, затратила {(time.perf_counter_ns() - start_time) / 1000}')
        return res

    return wrapped


@time_of_function
def make_dict(data):  # O(N)
    d = {}
    for el in data:  # O(N)
        d.setdefault(el[0], el[1])  # O(1)
    return d  # O(1)


@time_of_function
def make_list(data):  # O(N)
    l = []
    for el in data:  # O(N)
        l.append(el)  # O(1)
    return l


@time_of_function
def del_dict(d: dict):  # O(N)
    temp = d.copy()  # O(N)
    for k, _ in d.items():  # O(N)
        temp.pop(k)  # O(1)


@time_of_function
def del_list(l: list):  # O(N)
    temp = l.copy()  # O(N)
    for _ in temp:  # O(N)
        temp.pop()  # O(1)


@time_of_function
def update_dict(d: dict):  # O(N)
    temp = d.copy()  # O(N)
    for k, _ in d.items():  # O(N)
        temp.setdefault(k + 1, temp.pop(k) + 1)  # O(1)


@time_of_function
def update_dict_only_value(d: dict):  # O(N)
    temp = d.copy()  # O(N)
    for k, v in d.items():  # O(N)
        temp[k] = v + 1  # O(1)


@time_of_function
def update_list(l: list):  # O(N)
    temp = []
    temp.extend(l)  # O(N)
    # temp = list(l)
    # temp = l.copy()
    # temp = l[:]
    # print(id(temp), id(l))  # Я так и не понял почему происходит замена листа который приходит, id у них разный но
    # print(temp[0], l[0])  # когда проводишь манипуляции меняется temp и l, хотя l вообще не фигурирует тут
    # Для данной задачи не критично, но хотелось бы понять почему - так
    for idx, el in enumerate(temp):  # O(N)
        temp[idx][0] = el[0] - 1  # O(1)
        temp[idx][1] = el[1] + 1  # O(1)  #  Коментил эту строку что бы определить сколько меняется 1 значение что бы
        # не писать копи код, иначе может показаться что словарь в 2-3 раза быстрее добавляет значение
    # print(id(temp), id(l))
    # print(temp[0], l[0])


list_s = [[x, y] for x in random.sample(range(1, 1005), 560) for y in random.sample(range(0, 100000), 1)]
d = make_dict(list_s)  # O(N)
l = make_list(list_s)  # O(N)
del_dict(d)  # O(N)
del_list(l)  # O(N)
update_dict(d)  # O(N)
update_dict_only_value(d)  # O(N)
update_list(l)  # O(N)


"""
Исходя из класса сложности у всех он О(N), но при этом словарь выполнял все операции на порядок дольше, кроме одной,
    словарь чуть быстрее справился с внесением изменений в значение ключей, но если нужно поменять и ключ, 
    то операция начинала занимать примерно столько же что и при работе с листом.
Словарь долго меняет значения ключа, т.к. единственный способ это его удаление и добавление нового
Словарь долго собирается потому что у него значение ключа должно быть уникально
Словарь немного быстрее меняет значение т.к. ключи хранятся в виде хэша и по этому быстрее обращается к нему
Класс сложности - хорошо, но он не дает фактического представления о скорости работы функций
"""