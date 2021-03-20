# coding=utf-8

import math
# y = float(input())
# S = math.sqrt(math.cos(4 * y**2) + 7.151)
# print(S)
#
# y = float(input())
# N = 3 * y ** 2 + math.sqrt (y + 1)
# print(N)
# y = float(input())
# Z = 3 * y ** 2 + math.sqrt (y ** 3 + 1)
# print(Z)

# y = float(input())
# n = float(input())
# g = float(input())
# P = n * math.sqrt (y ** 3 + 1.09 * g)
# print(P)


# a = float(input("a: "))
# t = float(input("t: "))
#
# D = 9.8 * a**2 + 5.52 * math.cos(t**5)
#
# print(D)

# 6
# y = float(input('Vvedite y: '))
# x = float(input('Vvedite x: '))
# M = math.cos(2*y)+ 3.6*math.exp(x)
# print(M)


# a = float(input("Введите a: "))
# t = float(input("Введите t: "))
#
# D = 9.8 * a**2 + 5.52 + math.cos(t**5)
# print(D)

# n = int(input())
# k = int(input())
#
# time = 2 * n // k
#
# if 2 * n % k > 0:
#     time += 1
#
# print(time)

# def all_perms(elements):
#     if len(elements) <= 1:
#         yield elements
#     else:
#         for perm in all_perms(elements[1:]):
#             for i in range(len(elements)):
#                 yield perm[:i] + elements[0:1] + perm[i:]
#
#
# for i in all_perms([1, 3, 7, 9]):
#     print(i)

# lst = [1, 2, 5]
#
# mylist = [math.sqrt(x)*j for x in lst for j in range(5)]
# print(mylist)


# Графы

# class Vertex:
#
#     def __init__(self, value, connection=None):
#         self.value = value
#         self.ribs = []
#         if connection is not None:
#             self.ribs.append(connection)
#
#     def add_connection(self, connection):
#         if isinstance(connection, Vertex):
#             self.ribs.append(connection)
#             #connection.add_connection(self)
#
#     def __str__(self):
#         return str(self.value) \
#                + ", with count of connections " \
#                + str(len(self.ribs))
#
#
# a = Vertex(value=3)
# b = Vertex(value=4)
#
# a.add_connection(b)
# b.add_connection(a)
#
# print(b.ribs[0])
#
# class TreeVertex:
#
#     def __int__(self, value, right_child = None, left_child = None):
#         self.value = value
#         self.right_child = right_child
#         self.left_child = left_child
#
#     def set_right_child(self, item):
#         if isinstance(item, TreeVertex):
#             self.right_child = item
#
#     def set_left_child(self, item):
#         if isinstance(item, TreeVertex):
#             self.left_child = item


class TreeNode:
    def __init__(self, data, right=None, left=None):
        self.data = data
        self.right = right
        self.left = left

    def add_right_child(self, right_child):
        self.right = right_child

    def add_left_child(self, left_child):
        self.left = left_child

    def __str__(self):
        return str(self.data)


def go_around(tree: TreeNode):
    if tree.right is None and tree.left is None:
        print(tree.data)
        return None

    print(tree.data)
    if tree.right is not None:
        go_around(tree.right)
    if tree.left is not None:
        go_around(tree.left)


a = TreeNode(data=1)

a.right = TreeNode(data=3)
a.left = TreeNode(data=2)

a.left.right = TreeNode(data=6)
a.left.left = TreeNode(data=7)

a.right.right = TreeNode(data=4)
a.right.left = TreeNode(data=5)

a.left.right.left = TreeNode(data=8)

a.right.left.right = TreeNode(data=9)

go_around(a)
