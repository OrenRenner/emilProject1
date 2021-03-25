# coding=utf-8

import re

# re.match()
# re.search()
# re.findall()
# re.split()
# re.sub()
# re.compile()

# result = re.search(r'\d{4}-\d{2}-\d{2}', 'rfer 2021-03-17 Analytics Vidhya AV')
# print(result.start(), result.end(), result.group())
# r = result.group().split("-")
#
# for i, it in enumerate(r):
#     r[i] = int(it)
#
# print(r)


# def auto_num(string):
#     res = re.search(r'\w\d{3}\w{2}', string)
#     if res is not None:
#         print("Физ лицо")
#         return None
#     res = re.search(r'\d{3}\w{3}', string)
#     if res is not None:
#         print("Юр лицо")
#         return None
#     else:
#         print("Какая-та фигня!")
#         return None
#
# result = re.findall(r'[0-9A-Za-z]{1,40}@\w{1,20}\.\w{1,20}', '4rtff433@wef.wef, малако,\nИм0л0коИхлеб')
# print(result)

def Quick_Sort(array):
    if len(array)>1:
        pivot=array[0]
        low_index=1
        for i in range(0, len(array)):
            if array[i]<pivot:
                array[low_index], array[i] = array[i], array[low_index]
                low_index+=1
        array[low_index-1], array[0] = array[0], array[low_index-1]
        left_array = array[:low_index]
        pivot = array[low_index:low_index+1]
        right_array = array[low_index+1:]
        t_l = Quick_Sort(left_array)
        t_r = Quick_Sort(right_array)
        sorted_array = t_l + pivot + t_r
        return sorted_array
    else:
        return array


array=[1,5,3,7,2,4,9,6,8]
x=Quick_Sort(array)
print(x)