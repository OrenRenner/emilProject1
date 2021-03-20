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

a = "Привет как дела Все нормально спасибо как у тебя Да тоже нормально"
# with open("in.txt", "r") as file:
#     lines = file.readlines()
#     #print(lines)

lines = a.split(" ")
print(len(lines))
