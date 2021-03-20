# coding=utf-8

# def fact(n):
#     if n == 0:
#         return 1
#     f = 1
#     for k in range(1, n+1):
#         f = f*k
#     return f
#
# def fact1(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact1(n-1)
#
#
# def fibbonachi(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibbonachi(n-1) + fibbonachi(n-2)
#
#
# print(fibbonachi(7))

# x = float(input())
# y = float(input())
# #a
# if not (x <= -5 and x > 5):
#     print("Нормально!")
# else:
#     print("Не нормально!")
# #b
# if -3.5 <= y <= 8 and x != 0:
#     print("Нормально!")
# else:
#     print("Не нормально!")

# expirience = float(input())
# salary = float(input())
#
# if 2 <= expirience < 5:
#     salary += salary*0.02
# elif 5 <= expirience < 10:
#     salary += salary * 0.05
#
# print(salary)

import math
#
# x_0 = float(input())
# y_0 = float(input())
# x_1 = float(input())
# y_1 = float(input())
#
# dA = math.sqrt(x_0**2 + y_0**2)
# dB = math.sqrt(x_1**2 + y_1**2)
#
# if dA > dB:
#     print("Точка А удалена дальше")
# elif dA < dB:
#     print("Точка B удалена дальше")
# else:
#     print("Равноудалены")
#
# v1 = float(input("в м/c"))
# v2 = float(input("в км/ч"))
#
# v2 = v2 * 10 / 36
#
# if v1 > v2:
#     print("Первая скорость больше")
# elif v1 < v2:
#     print("Вторая скорость больше")
# else:
#     print("Равны")


# def powd(n, x):
#     if n == 1:
#         return x
#     return x * powd(n-1, x)
#
#
# n1 = int(input())
# x1 = float(input())
#
# print(powd(n1, x1))


# lst = [
#     [2, [3, 4], 1],
#     1,
#     5,
#     [4, 2, 1, [1, [4, 5]]],
#     [10]
# ]
#
# def sum_list(l):
#     if isinstance(l, int):
#         return l
#     sum = 0
#     for i in l:
#         sum += sum_list(i)
#     return sum
#
#
# print(sum_list(lst))
