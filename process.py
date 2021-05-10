# coding=utf-8
#
# import random, time, sys
# from multiprocessing import Process, Pipe
#
#
# # Зависимости, определенные ниже main()
#
# def main():
#     """
#     This is the main method in which we run parallel sorting!
#     """
#     N = 500000
#     if len(sys.argv) > 1:  # the user input a list size.
#         N = int(sys.argv[1])
#
#     # We want to sort the same list, so make a backup.
#     lystbck = [random.random() for x in range(N)]
#
#     # Sequential quicksort a copy of the list.
#     lyst = list(lystbck)  # copy the list
#     start = time.time()  # start time
#     lyst = quicksort(lyst)  # quicksort the list
#     elapsed = time.time() - start  # stop time
#
#     if not isSorted(lyst):
#         print('quicksort did not sort the lyst. oops.')
#
#     print('Sequential quicksort: %f sec' % (elapsed))
#
#     # So that cpu usage shows a lull.
#     time.sleep(3)
#
#     # Parallel quicksort.
#     lyst = list(lystbck)
#
#     start = time.time()
#     n = 3  # 2**(n+1) - 1 processes will be instantiated.
#     # I set the number of processes to be high since, with
#     # a random choice of pivot, it is unlikely the work
#     # will distribute evenly.
#
#     # Instantiate a Pipe so that we can receive the
#     # process's response.
#     pconn, cconn = Pipe()
#
#     # Instantiate a process that executes quicksortParallel
#     # on the entire list.
#     p = Process(target=quicksortParallel, \
#                 args=(lyst, cconn, n))
#     p.start()
#
#     lyst = pconn.recv()
#     # Blocks until there is something (the sorted list)
#     # to receive.
#
#     p.join()
#     elapsed = time.time() - start
#
#     if not isSorted(lyst):
#         print('quicksortParallel did not sort the lyst. oops.')
#
#     print('Parallel quicksort: %f sec' % (elapsed))
#
#     time.sleep(3)
#
#     # Built-in test.
#     # The underlying c code is obviously the fastest, but then
#     # using a calculator is usually faster too.  That isn't the
#     # point here obviously.
#     lyst = list(lystbck)
#     start = time.time()
#     lyst = sorted(lyst)
#     elapsed = time.time() - start
#     print('Built-in sorted: %f sec' % (elapsed))
#     #print(lyst)
#
#
# def quicksort(lyst):
#     """
#     quicksort implementation, return a new sorted version
#     of the input list.
#     Faster quicksort in that it relies on built-in list
#     comprehensions and concatenation.
#     Inspired from Vitalii Vanovschi:
#     http://www.parallelpython.com/component/option,com_smf/Itemid,1/action,printpage/topic,105.0
#     """
#     if len(lyst) <= 1:
#         return lyst
#     pivot = lyst.pop(random.randint(0, len(lyst) - 1))
#
#     return quicksort([x for x in lyst if x < pivot]) \
#            + [pivot] \
#            + quicksort([x for x in lyst if x >= pivot])
#
#
# def quicksortParallel(lyst, conn, procNum):
#     """
#     Partition the list, then quicksort the left and right
#     sides in parallel.
#     """
#
#     if procNum <= 0 or len(lyst) <= 1:
#         # In the case of len(lyst) <= 1, quicksort will
#         # immediately return anyway.
#         conn.send(quicksort(lyst))
#         conn.close()
#         return
#
#     # Create two independent lists (independent in that
#     # elements will never need be compared between lists).
#     pivot = lyst.pop(random.randint(0, len(lyst) - 1))
#
#     leftSide = [x for x in lyst if x < pivot]
#     rightSide = [x for x in lyst if x >= pivot]
#
#     # Creat a Pipe to communicate with the left subprocess
#     pconnLeft, cconnLeft = Pipe()
#     # Create a leftProc that executes quicksortParallel on
#     # the left half-list.
#     leftProc = Process(target=quicksortParallel, \
#                        args=(leftSide, cconnLeft, procNum - 1))
#
#     # Again, for the right.
#     pconnRight, cconnRight = Pipe()
#     rightProc = Process(target=quicksortParallel, \
#                         args=(rightSide, cconnRight, procNum - 1))
#
#     # Start the two subprocesses.
#     leftProc.start()
#     rightProc.start()
#
#     # Our answer is the concatenation of the subprocesses'
#     # answers, with the pivot in between.
#     conn.send(pconnLeft.recv() + [pivot] + pconnRight.recv())
#     conn.close()
#
#     # Join our subprocesses.
#     leftProc.join()
#     rightProc.join()
#
#
# def isSorted(lyst):
#     """
#     Return whether the argument lyst is in non-decreasing order.
#     """
#     for i in range(1, len(lyst)):
#         if lyst[i] < lyst[i - 1]:
#             return False
#     return True
#
#
# # Call the main method if run from the command line.
# if __name__ == '__main__':
#     main()

# import math
#
# n = 75
#
# print(math.log(n, 2))


# b = [14, 21, 125, 232, 2323, 53, 23, 978, 13, 4]

# for index, value in enumerate(b):
#     print(index, value)

# a = b.copy()
#
# a[0] = 3
# print(a)
# print(b)
#
# b[2] = 141
# print(a)
# print(b)



# print(b)
# b.append(342)
# print(b)
# b.insert(2, 999)
# print(b)
#
# if 5 in b:
#     b.remove(5)
# else:
#     print("Мы не смогли удалить!")
# print(b)
#
# b.pop(3)
# print(b)
# b = list()
# n = int(input())
# for i in range(n):
#     b.append(float(input()))

# b = [-1, 3, 5, 2, 45, -1, 34, 53]
# c = b.copy()
# c.sort(reverse=True)
# print(c[0])
#
# print(max(b))
#
# min = b[0]
# for i in b:
#     if min > i:
#         min = i
#
# print(min)


class Fraction:

    def __init__(self, numerate, denumerate):
        assert isinstance(numerate, int) and isinstance(denumerate, int) and numerate != 0
        self.numerate = numerate
        self.denumerate = denumerate
        if denumerate < 0:
            self.numerate *= -1
            self.denumerate *= -1

    def __str__(self):
        return str(self.numerate) + "/" + str(self.denumerate)

    def __add__(self, other):
        if isinstance(other, Fraction):
            return Fraction(
                numerate=self.numerate*other.denumerate + self.denumerate*other.numerate,
                denumerate=self.denumerate*other.denumerate
            )
        elif isinstance(other, int):
            return Fraction(
                numerate=self.numerate + self.denumerate * other,
                denumerate=self.denumerate
            )
        else:
            raise TypeError("unsupported operand type(s) for +: 'Fraction' and '" + str(type(other)) + "'")

    def __radd__(self, other):
        if isinstance(other, int):
            return Fraction(
                numerate=self.numerate + self.denumerate * other,
                denumerate=self.denumerate
            )
        else:
            raise TypeError("unsupported operand type(s) for +: 'Fraction' and '" + str(type(other)) + "'")

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(
                numerate=self.numerate*other.numerate,
                denumerate=self.denumerate*other.denumerate
            )
        elif isinstance(other, int):
            return Fraction(
                numerate=self.numerate * other,
                denumerate=self.denumerate
            )
        else:
            raise TypeError("unsupported operand type(s) for *: 'Fraction' and '" + str(type(other)) + "'")

    def __rmul__(self, other):
        if isinstance(other, int):
            return Fraction(
                numerate=self.numerate * other,
                denumerate=self.denumerate
            )
        else:
            raise TypeError("unsupported operand type(s) for *: 'Fraction' and '" + str(type(other)) + "'")

    def __sub__(self, other):
        if isinstance(other, Fraction):
            return Fraction(
                numerate=self.numerate * other.denumerate - self.denumerate * other.numerate,
                denumerate=self.denumerate * other.denumerate
            )
        elif isinstance(other, int):
            return Fraction(
                numerate=self.numerate - self.denumerate * other,
                denumerate=self.denumerate
            )
        else:
            raise TypeError("unsupported operand type(s) for -: 'Fraction' and '" + str(type(other)) + "'")

    def __rsub__(self, other):
        if isinstance(other, int):
            return Fraction(
                numerate=self.numerate - self.denumerate * other,
                denumerate=self.denumerate
            )
        else:
            raise TypeError("unsupported operand type(s) for -: 'Fraction' and '" + str(type(other)) + "'")

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            return Fraction(
                numerate=self.numerate * other.denumerate,
                denumerate=self.denumerate * other.numerate
            )
        elif isinstance(other, int):
            return Fraction(
                numerate=self.numerate,
                denumerate=self.denumerate * other
            )
        else:
            raise TypeError("unsupported operand type(s) for /: 'Fraction' and '" + str(type(other)) + "'")

    def __rtruediv__(self, other):
        if isinstance(other, int):
            return Fraction(
                numerate=self.numerate,
                denumerate=self.denumerate * other
            )
        else:
            raise TypeError("unsupported operand type(s) for /: 'Fraction' and '" + str(type(other)) + "'")

    def my_func(self):
        #Реализовать функцию сокращения
        pass


a = Fraction(numerate=2, denumerate=4)
b = Fraction(numerate=1, denumerate=3)
print(a / b)


class Time:

    def __init__(self, hours, minutes, seconds, format):
        pass


a = Time()
print(a)