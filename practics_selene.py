# coding=utf-8
# !/usr/bin/python

import random, time, sys
import multiprocessing
from multiprocessing import Process, Pipe


def main(argv):
    #filename argv[0]
    #count of value int(argv[1])
    N = int(argv[1])
    with open(argv[0], "r") as myfile:
        lyst = [float(next(myfile)) for _ in range(N)]

    start = time.time()
    n = multiprocessing.cpu_count()

    pconn, cconn = Pipe()

    p = Process(target=quicksortParallel, \
                args=(lyst, cconn, n))
    p.start()

    lyst = pconn.recv()

    p.join()
    elapsed = time.time() - start

    with open("out.txt", "w") as file:
        out_str = ""
        for i in lyst:
            out_str += str(i) + "\n"

        file.write(out_str)

    if not isSorted(lyst):
        print('quicksortParallel did not sort the lyst. oops.')

    print('Parallel quicksort: %f sec' % (elapsed))


def quicksort(lyst):
    if len(lyst) <= 1:
        return lyst
    pivot = lyst.pop(random.randint(0, len(lyst) - 1))

    return quicksort([x for x in lyst if x < pivot]) \
           + [pivot] \
           + quicksort([x for x in lyst if x >= pivot])


def quicksortParallel(lyst, conn, procNum):
    if procNum <= 0 or len(lyst) <= 1:
        conn.send(quicksort(lyst))
        conn.close()
        return

    pivot = lyst.pop(random.randint(0, len(lyst) - 1))

    leftSide = [x for x in lyst if x < pivot]
    rightSide = [x for x in lyst if x >= pivot]

    pconnLeft, cconnLeft = Pipe()
    leftProc = Process(target=quicksortParallel, \
                       args=(leftSide, cconnLeft, procNum - 1))

    pconnRight, cconnRight = Pipe()
    rightProc = Process(target=quicksortParallel, \
                        args=(rightSide, cconnRight, procNum - 1))

    leftProc.start()
    rightProc.start()

    conn.send(pconnLeft.recv() + [pivot] + pconnRight.recv())
    conn.close()

    leftProc.join()
    rightProc.join()


def isSorted(lyst):
    for i in range(1, len(lyst)):
        if lyst[i] < lyst[i - 1]:
            return False
    return True


if __name__ == '__main__':
    main(sys.argv[1:])
