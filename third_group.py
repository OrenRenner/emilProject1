# coding=utf-8

import math
#
# D = float(input())
#
# if D > 0:
#     A = 2
#     Atmp = (2 + 1/(A))
#     count = 0
#     while math.fabs(A - Atmp) < D:
#         A = Atmp
#         Atmp = (2 + 1 / (A))
#         count += 1
#
#     print(count)
# else:
#     print("Число D меньше нуля")


# maxd = 0
#
# while n > 0:
#     if maxd < n % 10:
#         maxd = n % 10
#     n //= 10
#
# print(maxd)

# n = int(input())
# new_n = 0
# old_n = n
#
# while n > 0:
#     new_n *= 10
#     new_n += n % 10
#     n //= 10
#
# if new_n == old_n:
#     print("Симметрично")
# else:
#     print("Не симметрично")

# A = float(input())
# N = int(input())
#
# for_pow = 1
# for i in range(N):
#     for_pow *= A
#
# print(for_pow)

# N = int(input())
#
# for i in range(1, N+1):
#     if i % 5 != 0 and i % 3 == 0:
#         tmp_sum = 0
#         tmp_num = i
#         while tmp_num > 0:
#             if tmp_num % 10 == 9:
#                 continue
#             tmp_sum += tmp_num % 10
#             tmp_num //= 10
#         if tmp_sum % 5 != 0 and tmp_sum % 3 == 0:
#             print(i)

# a = {
#     "1": 1,
#     "2": 2,
#     "3": 3,
#     "7": 7
# }
#
# b = {
#     "3": 3,
#     "4": 4,
#     "5": 5,
#     "6": 6
# }
#
# c = dict()
#
# for key_a, value_a in a.items():
#     for key_b, value_b in b.items():
#         c[key_a] = value_a
#         c[key_b] = value_b
#
# print(c)

# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
#
# max_d = my_dict['a']
#
# for i in my_dict.values():
#     if max_d < i:
#         max_d = i
#
# print(max_d)

# a = 234213424
# s = ''
#
# while a > 0:
#     s += str(a%2)
#     a //= 2
# a = list(s)
# a.reverse()
# print("".join(a))


# Задача 1
# Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
# Выведите все элементы, которые меньше 5.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
# for i in a:
#     if i < 5:
#         print(i)


# Задача 2
# Даны списки:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
# Нужно вернуть список, который состоит из элементов, общих для этих двух списков.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# set_a = set(a)
#
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# set_b = set(b)
#
# c = set_a.intersection(set_b)
# print(list(c))

# Задача 3
# Отсортируйте словарь по значению в порядке возрастания и убывания.

# a = {
#     "1": 2,
#     "2": 1,
#     "3": 4,
#     "4": 3
# }
# lst = []
#
# for i in a.values():
#     lst.append(i)
#
# lst.sort()
# print(lst)
#
# for index, item in enumerate(lst):
#     a[str(index + 1)] = item
#
# print(a)

# Задача 4
# Напишите программу для слияния нескольких словарей в один.

# a = {
#     "1": 1,
#     "2": 2
# }
# b = {
#     "3": 3,
#     "4": 4
# }
# for key, value in b.items():
#     a[key] = value
#
# print(a)

# Задача 5
#
# Найдите три ключа с самыми высокими значениями в словаре

# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
# lst = []
# for key, val in my_dict.items():
#     lst.append(val)
#
# lst.sort()
# lst_key = []
# for i in lst[-3:]:
#     for j in my_dict:
#         if my_dict[j] == i:
#             lst_key.append(j)
#
# print(set(lst_key))


# class MyClass:
#     item = 12
#
#     def print_item(self):
#         print(self.item)
#
#     def hello(self, value):
#         print("Hello,", value)
#
#
# a = MyClass()
# a.hello("232323")
# a.hello("wregegregergreg")
# print(a.item)
# a.print_item()
# a.item = 32323
# a.print_item()
# print(a.item)
#
# b = MyClass()
# b.hello("wefbeyfge")


# class Person:
#
#     def __init__(self, name):
#         self.name = name
#
#     def say_name(self):
#         print(self.name)
#
#
# a = Person(name="Emil")
# a.say_name()
#
# a.name = "Gosha"
# a.say_name()

# class Money:
#
#     def __init__(self, nominal, count, valuta):
#         self.nominal = nominal
#         self.count = count
#         self.valuta = valuta
#
#     def find_sum(self):
#         return self.nominal * self.count
#
#     def print_val(self):
#         print(self.valuta)
#
#
# a = Money(nominal=200, count=30, valuta="Dollar")
# f = a.find_sum()
# a.print_val()
# print(f)

# x = int(input())
#
# for i in range(2, x+1):
#     sum = 0
#     for j in range(1, i):
#         if i % j == 0:
#             sum += j
#
#     if sum == i:
#         print(i)

# a = int(input())
# b = int(input())
# c = min(a, b)
# nod = 1
# for i in range(2, c+1):
#     if a % i == 0 and b % i == 0:
#         nod = i
# if nod == 1:
#     print("Взаимно простые")

# n = int(input())
#
# for i in range(2, n+1):
#     for j in range(2, n+1):
#         nod = 1
#         for k in range(2, min(i, j) + 1):
#             if i % k == 0 and j % k == 0:
#                 nod = k
#         if nod == 1 and i != j:
#             print(i, j)


# n = int(input())
#
# if 100000 <= n <= 999999:
#     pass
# else:
#     print("Не верно введенное число")


# for i in range(1, 13):
#     pass
# else:
#     pass
# counter = 0
# for k in range(100000, 1000000):
#     n = k
#     sum1 = 0
#     sum2 = 0
#     for i in range(3):
#         sum1 += n % 10
#         n //= 10
#     for i in range(3):
#         sum2 += n % 10
#         n //= 10
#
#     if sum1 == sum2:
#         counter += 1
#         print(k)
#
# print(counter)
a = 9


def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10

    return sum


def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact


def my_func(a, b, c, d, e, f):
    assert isinstance(a, int) and isinstance(b, float)
    if a > 0:
        s1 = a + b
        s2 = c + d + e + f
        return "None"
    else:
        return "High"



print(my_func(d=4, e=5, f=7, a=-1, b=2.0, c=3))

