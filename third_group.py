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


def four_oper(a, b):
    sum = a + b
    mul = a * b
    div = a / b
    sub = a - b
    return sum, sub, mul, div

#10111213..9899

# num = 10
#
# for i in range(11, 100):
#     num *= 100
#     num += i
#
# print(num)

import random


# def f(a, b):
#     if not (isinstance(a, int) and isinstance(b, int)):
#         raise TypeError("Ввел не тот тип данных")
#     return int(a % b == 0 or b % a == 0)
#
# print(f(0, 5))
#
# class TreeNode:
#     def __init__(self, data, right=None, left=None, mid_right=None, mid_left=None):
#         assert not isinstance(data, int) \
#             or not isinstance(right, TreeNode) \
#             or not isinstance(left, TreeNode) \
#             or not isinstance(mid_right, TreeNode) \
#             or not isinstance(mid_left, TreeNode)
#         self.data = data
#         self.right = right
#         self.left = left
#         self.mid_left = mid_left
#         self.mid_right = mid_right
#
#     def add_right_child(self, right_child):
#         assert isinstance(right_child, TreeNode)
#         self.right = right_child
#
#     def add_left_child(self, left_child):
#         assert isinstance(left_child, TreeNode)
#         self.left = left_child
#
#     def add_mid_right_child(self, mid_right_child):
#         assert isinstance(mid_right_child, TreeNode)
#         self.mid_right = mid_right_child
#
#     def add_mid_left_child(self, mid_left_child):
#         assert isinstance(mid_left_child, TreeNode)
#         self.mid_left = mid_left_child
#
#     def __str__(self):
#         return str(self.data)
#
# def go_around(tree: TreeNode):
#     if tree.left is None and tree.right is None \
#        and tree.mid_left is None and tree.mid_right is None:
#         print(tree.data)
#         return None
#     print(tree.data)
#     if tree.left is not None:
#         go_around(tree.left)
#     if tree.right is not None:
#         go_around(tree.right)
#     if tree.mid_left is not None:
#         go_around(tree.mid_left)
#     if tree.mid_right is not None:
#         go_around(tree.mid_right)
#
#
# a = TreeNode(data=1)
#
# a.right = TreeNode(data=3)
# a.left = TreeNode(data=2)
#
# a.mid_left = TreeNode(data=10)
# a.mid_right = TreeNode(data=11)
#
# a.left.right = TreeNode(data=6)
# a.left.left = TreeNode(data=7)
#
# a.left.mid_left = TreeNode(data=12)
# a.left.mid_right = TreeNode(data=13)
#
# a.right.right = TreeNode(data=4)
# a.right.left = TreeNode(data=5)
#
# a.right.mid_left = TreeNode(data=14)
# a.right.mid_right = TreeNode(data=15)
#
# a.left.right.left = TreeNode(data=8)
# a.right.left.right = TreeNode(data=9)
#
# go_around(a)


def factorial1(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact


def factorial2(size):
    if size <= 1:
        return 1
    else:
        return size * factorial2(size-1)


def is_odd1(n):
    if n % 2 == 0:
        return True
    else:
        return False


def is_odd2(n):
    if n == 1:
        return False
    elif n == 2:
        return True

    return is_odd2(n-2)


def convert_binary(n):
    if n == 1:
        return str(n)
    else:
        return str(n % 2) + convert_binary(n//2)


def sum_of_lst(lst):
    tmp_sum = 0
    for i in lst:
        if isinstance(i, list):
            tmp_sum += sum_of_lst(i)
        elif isinstance(i, int):
            tmp_sum += i
        else:
            raise TypeError("Введен не тот тип данных!")

    return tmp_sum


# a = [
#     [1, [2, 3, 4], [5, 7]],
#     [1, 6.7],
#     [4],
#     4,
#     [11, 67, [5]], 8, 9
# ]
#
# print(sum_of_lst(a))




def bifshteks(n, k):
    if isinstance(n, int) and isinstance(k, int):
        if 1 <= n <= 100 and 1 <= k <= 100:
            return n*k*2
        else:
            raise ValueError("Вышли за интервал!")
    else:
        raise TypeError("Введены не те типы данных!")


def my_sum(n):
    if isinstance(n, int):
        if -10000 <= n <= 10000:
            s = 0
            if n > 1:
                for i in range(1, n+1):
                    s += i
            elif n == 1:
                return 1
            else:
                for i in range(n, 2):
                    s += i
            return s
        else:
            raise ValueError("Вышли за интервал!")
    else:
        raise TypeError("Введен не тот тип данных!")

#
# print(my_sum(-3))


# lst = ['белое вино', 'салат Цезарь', 'паста Карбонара', 'чизкейк', 'шоколадный сорбет']
#
# a = input()
# b = input()
#
# if a in lst:
#     lst[lst.index(a)] = b
#     print(lst)
# else:
#     print("Введенное не существует!")

# def menu_changer(menu: list):
#     menu_dict = dict()
#     for i in menu:
#         menu_dict[i] = i
#     q = str(input("Change menu?  "))
#     if q == "Yes" or "yes":
#         itr = str(input("Type item to replace:"))
#         ni = str(input("Type new item:"))
#         menu_dict[itr] = ni
#         menu.clear()
#         for i in menu_dict:
#             menu.append(menu_dict[i])
#         return menu
#     else:
#         return "Menu remained unchanged"
#
#
# print(menu_changer(['красное вино', 'салат Цезарь', 'паста Карбонара', 'чизкейк', 'шоколадный сорбет']))

#
# diary = {
#     'понедельник': {
#                           'утро': ['погулять с собакой'],
#                           'день': [],
#                           'вечер': ['погулять с собакой']
#                                       },
#     'вторник': {
#                       'утро': ['погулять с собакой'],
#                       'день': [],
#                       'вечер': ['погулять с собакой']
#                                   },
#     'среда': {
#                       'утро': ['погулять с собакой'],
#                       'день': [],
#                       'вечер': ['погулять с собакой']
#                                   },
#     'четверг': {
#                       'утро': ['погулять с собакой'],
#                       'день': [],
#                       'вечер': ['погулять с собакой']
#                                   },
#     'пятница': {
#                       'утро': ['заехать в шиномонтаж', 'помыть машину'],
#                       'день': [],
#                       'вечер': ['поход в театр',  'ужин в кафе']
#                                   },
#     'суббота': {
#                       'утро': [],
#                       'день': [],
#                       'вечер': []
#                                   },
#     'воскресенье': {
#                       'утро': [],
#                       'день': [],
#                       'вечер': []
#                                   }
# }
#
# diary['среда']['утро'].pop(0)
# diary['среда']['вечер'].pop(0)
# diary['среда']['утро'].pop(0)
# diary['среда']['вечер'].pop(0)
# # t = ('суббота', 'воскресенье')
# # del diary['суббота']
# # del diary['воскресенье']
# # diary[t] = ['посадить цветы на даче']
# #
# #
# # diary['вторник']['утро'].append('поход к зубному')
# # print(diary)
#
# def first(d1, d2):
#     new_dict = d1.copy()
#     for i in d2:
#         if i in new_dict:
#             new_dict[i] = min(new_dict[i], d2[i])
#         else:
#             new_dict[i] = d2[i]
#
#     return new_dict
# #
# #
# # a = {
# #     "1": 4,
# #     "5": 1,
# #     "2": 5
# # }
# #
# # b = {
# #     "3": 1,
# #     "5": 6,
# #     "2": 2,
# #     "7": 10
# # }
# #
# # print(first(a, b))
#
#
# # users = {"Tom", "Bob", "Alice", "Tom", "Alice"}
# # u2 = {'Alice', 'Tom', 'Bob'}
# # print(users)
# # users.add("Tom")
# # print(users)
# #
# # user = "Tim"
# # users.discard("wrgfwgf4w")
#
#
# # users1 = {"Tom", "Bob", "Alice"}
# # users2 = {"Sam", "Kate", "Bob"}
# #
# # print(users1 | users2)
# # print(users1 & users2)
#
#
#
#
# def my_func(a, b):
#     res = (
#         a+b,
#         a-b,
#         a*b,
#         a/b,
#         a//b,
#         a%b,
#         a**b,
#
#         a > b,
#         a < b,
#         a >= b,
#         a <= b,
#         a != b,
#         a == b
#     )
#     return res
#
# print(my_func(33, 23))
#
#
#


#file = open("D:/images/ytdtrde.txt", "a")

lst = []
import math

# with open("in2.txt", "w") as file1:
#     file1.write("")
#
# with open("myfile.txt", "r") as file:
#     for i in file:
#         try:
#             a = float(i)
#             if a < 0:
#                 with open("in2.txt", "a") as file1:
#                     file1.write(str(a) + "\n")
#         except Exception as ex:
#             print(ex)


# n = int(input())
#
# while n > 1:
#     for i in range(2, n+1):
#         if n % i == 0:
#             print(i)
#             n //= i

# n = int(input())
#
# n += 1
# while True:
#     is_simple = False
#     for i in range(2, n):
#         if n % i == 0:
#             is_simple = False
#             break
#         is_simple = True
#
#     if is_simple:
#         print(n)
#         break
#     else:
#         n += 1


m = 60
N = int(input())
percent = int(input())

N += N*percent/100
c = N*0.2
N -= N*0.2
print(c)
print(N/m)


import datetime



























