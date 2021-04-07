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

# list_of_words = []
# count_of_words = {}
# out_str = ""
#
# with open("in.txt", "r") as file:
#     in_str = file.read()
#     in_str = in_str.replace(".", "").replace(",", "").replace("!", "").replace("?", "")
#     in_str = in_str.lower()
#     list_of_line = in_str.split("\n")
#
#     for i in list_of_line:
#         list_of_words += i.split()
#
#     for word in list_of_words:
#         if word in count_of_words:
#             count_of_words[word] += 1
#         else:
#             count_of_words[word] = 1
#
#     for key, value in count_of_words.items():
#         out_str += str(key) + " - " + str(value) + "\n"
#         print(str(key) + " - " + str(value))
#
# with open("out.txt", "w") as file:
#     file.write(out_str)



import math
#n!
# def factorial(n):
#     f = 1
#     for i in range(1, n+1):
#         f *= i
#     return f


# g = math.cos(131)
# print(g)
# t = factorial(10)
# print(t)
# print(factorial(3))
# print(factorial(7))

# def nod(a, b):
#     i = 1
#     for j in range(1, min(a, b)+1):
#         if a % j == 0 and b % j == 0:
#             i = j
#     return i


# g1 = nod(12, 4)
# g2 = nod(108, 96)
# print(g1, g2)
# a = 3
# def sum(lst):
#     if isinstance(lst, list):
#         sums = 0
#         for i in lst:
#             sums += i
#         return sums/len(lst)
#     else:
#         return "Ты подал не того типа"
#
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(sum(a))
#
# b = [14, 2, -43, 4, 35, 6, 7, 28, 89]
# print(sum(b))
#
# с = 1212
# print(sum(с))

# lst_int = []
# char = ''
#
# while char != '.':
#     char = input()
#     if char != '.':
#         lst_int.append(int(char))
#
# print(sum(lst_int))


# def area_triangule(a, b):
#     if a > 0 and b > 0:
#         S = a*b/2
#         return S
#     else:
#         return "Заданы неверные стороны"
#
#
# print(area_triangule(-3, 4))
#
# #a, b, S-? S = a*b/2
# a = [1, 2, 3, 4, 5, 6, 7]


# class Date:
#
#     def __init__(self, year, month, day):
#         assert 1 <= month <= 12 \
#                and 1 <= day <= 30 \
#                and year > 1900 \
#                and isinstance(year, int) \
#                and isinstance(month, int) \
#                and isinstance(day, int)
#         self.year = year
#         self.month = month
#         self.day = day
#
#     def __str__(self):
#         string = str(self.year)
#         if self.month < 10:
#             string += "-0" + str(self.month)
#         else:
#             string += "-" + str(self.month)
#
#         if self.day < 10:
#             string += "-0" + str(self.day)
#         else:
#             string += "-" + str(self.day)
#
#         return string
#
#     def __add__(self, other):
#         assert isinstance(other, Date)
#         year_tmp = self.year + other.year
#         month_tmp = self.month + other.month
#         day_tmp = self.day + other.day
#
#         if day_tmp > 30:
#             month_tmp += 1
#             day_tmp -= 30
#
#         if month_tmp > 12:
#             year_tmp += 1
#             month_tmp -= 12
#
#         if month_tmp > 12:
#             year_tmp += 1
#             month_tmp -= 12
#
#         return Date(year=year_tmp,
#                     month=month_tmp,
#                     day=day_tmp)
#
#     def __sub__(self, other):
#         assert isinstance(other, Date)
#         year_tmp = self.year - other.year
#         month_tmp = self.month - other.month
#         day_tmp = self.day - other.day
#         assert year_tmp >= 0
#         if month_tmp < 0:
#             month_tmp += 12
#             year_tmp -= 1
#         if day_tmp < 0:
#             day_tmp += 30
#             month_tmp -= 1
#         if month_tmp < 0:
#             month_tmp += 12
#             year_tmp -= 1
#         assert year_tmp > 0
#         return Date(year=year_tmp,
#                     month=month_tmp,
#                     day=day_tmp)
#
#     def __mul__(self, other):
#         assert isinstance(other, int)
#         pass
#
#     def __int__(self):
#         pass
#
# a = Date(year=2021, month=11, day=20)
# print(a)
#
# b = Date(year=2020, month=3, day=17)
# print(b)


# to_be_sorted = [4, 1, 43, 553, 673, 635, 67, 2, 45, 0]
# length = len(to_be_sorted)
# for i in range(length):
#     for j in range(length):
#         for k in range(length):
#             pass
#         if to_be_sorted[j] > to_be_sorted[i]:
#             temporary = to_be_sorted[j]
#             to_be_sorted[j] = to_be_sorted[i]
#             to_be_sorted[i] = temporary
#
#
# for i in range(length):
#     for j in range(length):
#         if to_be_sorted[j] > to_be_sorted[i]:
#             temporary = to_be_sorted[j]
#             to_be_sorted[j] = to_be_sorted[i]
#             to_be_sorted[i] = temporary
#
# a = int(input())
# print(a)
#
# print(to_be_sorted)




# def factorial(n):
#     if n == 0:
#         return 1
#
#     return n * factorial(n-1)
#
#
#
# print(factorial(4))

# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
#
#
# print(fib(5))


def nod(a, b):
    if b % a == 0:
        return a
    elif a % b == 0:
        return b
    else:
        if a < b:
            return nod(b%a, b)
        else:
            return nod(a%b, a)


print(nod(13, 17))


# Python program for implementation of Quicksort Sort

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot


def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort


def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

    # Driver code to test above


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
print(arr),


a = [
    [1, 2, 3, 4, [5]],
    3, 5, 7,
    [1, 2],
    [4],
    [[[4]], 6],
    10, 11,
    [10, 11]
]