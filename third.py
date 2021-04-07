# coding=utf-8

n = int(input())

for i in range(1, n+1):
    i_square = i**2
    i_clone = i

    flag = False
    while i_clone > 0:
        if i_clone % 10 == i_square % 10:
            flag = True
        else:
            flag = False
            break
        i_square //= 10
        i_clone //= 10


    print(i, i ** 2)
    if flag:
        print("Является")
    else:
        print("Не является")