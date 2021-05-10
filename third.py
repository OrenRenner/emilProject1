# coding=utf-8
# !/usr/bin/python

# import sys
# import getopt
#
#
# def main(argv):
#     print(argv[0])
#     print(argv[1])
#
#
# if __name__ == "__main__":
#     main(sys.argv[1:])
import random

# lystbck = [random.random()*10 for x in range(50000)]
#
# with open("in.txt", "w") as file:
#     out_str = ""
#     for i in lystbck:
#         out_str += str(i) + "\n"
#
#     file.write(out_str)

# print(31, 18, 9)

# a = int(input())
#
# print(a, "- Вот какое число Вы ввели")


# x = float(input())
# y = 17 * x**2 - 6 * x + 13
# print(y)

def my_func(a:list):
    if isinstance(a, list):
        mean = 0.0
        for i in a:
            mean += i
        mean /= len(a)
        return mean
    else:
        raise TypeError("Параметр не типа list!")


def sort_list(lst:list):
    if isinstance(lst, list):
        for i in range(len(lst)):
            max = lst[i]
            max_index = i
            for j in range(i, len(lst)):
                if max < lst[j]:
                    max = lst[j]
                    max_index = j
            lst[i], lst[max_index] = lst[max_index], lst[i]
        return lst
    else:
        raise TypeError("Параметр не типа list!")



def get_max_index(lst:list):
    if isinstance(lst, list):
        max = lst[0]
        max_index = 0
        for j in range(len(lst)):
            if max < lst[j]:
                max = lst[j]
                max_index = j

        return max, max_index


def get_index(lst:list):
    if isinstance(lst, list):
        for i, item in enumerate(lst):
            if item % 2 == 0:
                return i


# import math as m
# num=int(input('Write a number: '))
# pow_num=1
# while m.pow(pow_num, 2)<num:
#     if m.sqrt((num+m.pow(pow_num, 2)))%1==0:
#         print('Yes')
#         break
#     else:
#         pow_num+=1
# else:
#     print('No')

def Evklid(a, b):
    if a % b == 0:
        print(b, 'is GCD')
    else:
        Evklid(b, a % b)
#
#
# a = int(input('Write a number(a): '))
# b = int(input('Write a number(b): '))
# Evklid(a, b)

def Eratos(n):
    array = []

    for i in range(n + 1):
        array.append(i)

    for i in array:
        if i > 1:
            for j in range(i + i, len(array), i):
                array[j] = 0

    array = [i for i in array if i != 0 and i != 1]
    return array
#
#
# lst = Eratos(50)
# print(lst)
#
#
# import math
#
# def Ferma(n:int):
#     if n % 2 == 0 and n != 2:
#         return True, 2, n//2
#     else:
#         for i in range(1, (n - 1)//2 + 1):
#             s = n + i**2
#             tmp = math.sqrt(s)
#             if tmp.is_integer() and int(tmp) - i > 1:
#                 return True, i, int(tmp)
#
#         return False, None, None
#
#
# for i in lst:
#     print(Ferma(i))

import numpy as np


def transpose(a):
    a_new = np.empty((a.shape), dtype=a.dtype)
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            a_new[j][i] = a[i][j]

    return a_new

a = np.array(
    [
        [2, 1, 7, 4],
        [5, 6, 7, 3],
        [9, 8, 2, 12],
        [11, 14, 15, 15]
    ]
)

print(transpose(a))

