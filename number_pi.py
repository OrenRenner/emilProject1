#!/usr/bin/env python
# coding=utf-8


# if __name__ == "__main__":
#     main()

# import my_module
#
# print(my_module.nominals(4343346.34))
#
# my_module.main()

# import os
# import time
#
# print("о чем вам напомнить?")
# text = str(input())
# print("через сколько минут?")
# local_time = float(input())
# local_time = local_time * 60
# time.sleep(local_time)
#
# print(text)
# os.startfile('audio.mp3')

# st="Aaron Smith  wfwe    fwef   sefwefw"
#
# lst = []
#
# count = 0
#
# for i in st:
#     if i == " ":
#         count += 1
#     else:
#         if count != 0:
#             lst.append(count)
#         count = 0
#
# print(max(lst))

# str = "ddddhhhh44444ggggggggggffgggggggggggggggweeeeeee333"
# last_symbol = str[0]
# count = 1
# lst_for_counts = []
# for i in str[1:]:
#     if i == last_symbol:
#         count += 1
#     else:
#         if count != 0:
#             lst_for_counts.append(count)
#         count = 0
#         last_symbol = i
# print(lst_for_counts)


# str = "qwergtyuiopasdfg12457"
#
# s = set()
# for i in str:
#     if i in s:
#         print(i)
#         break
#     else:
#         s.add(i)

# s1 = "iirnformation"
# s2 = "data analis"
#
# s1_l = set(s1)
# s2_l = set(s2)
# print(s1_l or s2_l)
#
# for i in s1_l:
#     print(i in s2, end=" ")

import random

first_name = input()
# middle_name = input()

in1 = random.randint(0, len(first_name) - 1)
in2 = random.randint(0, len(first_name) - 1)

out_str = ""

if in1 > in2:
    out_str = first_name[:in2] + first_name[in1] + first_name[in2+1:in1] + first_name[in2] + first_name[in1+1:]
else:
    out_str = first_name[:in1] + first_name[in2] + first_name[in1 + 1:in2] + first_name[in1] + first_name[in2 + 1:]

print(out_str[0].upper() + out_str[1:].lower())

