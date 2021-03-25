# coding=utf-8
#
# class Fraction:
#
#     def __init__(self, numerator, denumerator):
#         assert isinstance(numerator, int) \
#                and isinstance(denumerator, int) \
#                and denumerator > 0
#         self.numerator = numerator
#         self.denumerator = denumerator
#
#     def __str__(self):
#         return str(self.numerator) + "/" + str(self.denumerator)
#
#     def __add__(self, other):
#         if isinstance(other, Fraction):
#             return Fraction(
#                 numerator=self.numerator*other.denumerator\
#                           + self.denumerator*other.numerator,
#                 denumerator=self.denumerator*other.denumerator
#             )
#         elif isinstance(other, int):
#             return Fraction(
#                 numerator=self.numerator + self.denumerator * other,
#                 denumerator=self.denumerator
#             )
#
#
#
# try:
#     a = Fraction(numerator=1, denumerator=2)
#     b = Fraction(numerator=1, denumerator=3)
#     print(a + 6)
# except:
#     print("Error")


# a = int(input())
# b = int(input())
#
# print(a >= b)
# print(a > b)
# print(a <= b)
# print(a < b)
# print(a == b)
# print(a != b)
#
# n = int(input())
# k = int(input())
# a = []
#
# for i in range(n):
#     a.append(int(input()))
#
# summa_bum = 0
# summa_droid = 0
#
# for i in a:
#     if k - i < 0:
#         summa_bum += i - k
#     else:
#         summa_droid += k - i
#
# print(summa_bum)
# print(summa_droid)

# n = int(input())
#
# a = []
# for i in range(n):
#     a.append(int(input()))
#
#
# mean_mark = 0.0
# flag_is_three = False
#
# for i in a:
#     if i == 3:
#         print("None")
#         flag_is_three = True
#         break
#     else:
#         mean_mark += i
#
# mean_mark /= n
#
# if not flag_is_three:
#     if mean_mark == 5:
#         print("Named")
#     elif mean_mark >= 4.5:
#         print("High")
#     else:
#         print("Simple")

#
# r = 'Hello! .rer|q ererg|er? , .erg!rgerg'
#
# a = r.replace('!', '').replace('.', '').replace(',', '').replace('?', '')
# print(a)
# print(r)

#a = "Привет как дела Все нормально спасибо как у тебя Да тоже нормально"
# with open("in.txt", "r") as file:
#     lines = file.readlines()
#     #print(lines)

# lines = a.split(" ")
# print(len(lines))

# a = int(input())
# b = int(input())
#
# if a < 0:
#     a *= -1
#
# if b < 0:
#     b *= -1
#
# print((a + b) * 0.5)


# year = int(input())
#
# if -2000 <= year <= 2000:
#     if year % 4 == 0:
#         print("366 дней в", year, "году")
#     else:
#         print("365 дней в", year, "году")

# str_tmp = ""
# #527545454545454544554
# while str_tmp != "Yes":
#     str_tmp = input()
#     print(str_tmp)

# number = 123456787654321234567890987654567898765456543
# summ = 0
# while number > 0:
#     summ += number % 10
#     number //= 10

# summ = 0.0
#
# for i in range(-10, 21):
#     if i == 0:
#         continue
#     summ += 1 / i
#
# print(summ)


#
# if A < B:
#     count = 0
#     for i in range(B-1, A, -1):
#         print(i)
#         count += 1
#
#     print(count)

# A = float(input())
# N = int(input())
#
# if N > 0:
#     for_mul = 1.0
#     for i in range(N):
#         for_mul *= A
#     print(for_mul)

# n = int(input())
# res = 0
#
# for i in range(1, n+1):
#     res += i
#
# if res % 2 == 0:
#     print("black")
# else:
#     print("grimmy")

class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = []

    def add_edge(self, vertex):
        if isinstance(vertex, Vertex):
            self.edges.append(vertex)
        else:
            return "Error Type"

    def __str__(self):
        return str(self.value)

a = Vertex(value=3)
b = Vertex(value=4)
a.add_edge(b)
b.add_edge(a)

c = Vertex(value=7)
c.add_edge(b)
b.add_edge(c)

d = Vertex(value=5)
d.add_edge(b)
b.add_edge(d)

d.add_edge(c)
c.add_edge(d)


def graph_traversal(item:Vertex, lst:list):
    for i in item.edges:
        for j in lst:
            if i == j:
                return
        print(i)
        lst.append(i)
        graph_traversal(i, lst)

t = []
graph_traversal(b, t)