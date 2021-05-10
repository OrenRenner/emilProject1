import multiprocessing
import random, time, sys
from multiprocessing import Pool, Process, Pipe
from itertools import chain


def main(argv):

    N = int(argv[1])
    with open(argv[0], "r") as myfile:
        lyst = [float(next(myfile)) for _ in range(N)]

    start = time.time()
    n = multiprocessing.cpu_count()
    lyst = quicksortParallel(lyst, n)
    elapsed = time.time() - start
    print('Parallel quicksort: %f sec' % (elapsed))

    with open("result.txt", "w") as file:
        out_str = ""
        for i in lyst:
            out_str += str(i) + "\n"
        file.write(out_str)


def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


def partition(a, lo, hi):
    rnd = random.randint(lo, hi)
    pivot = a[rnd]
    swap(a, hi, rnd)
    b = lo
    for i in range(lo, hi):
        if a[i] < pivot:
            swap(a, i, b)
            b += 1
    swap(a, hi, b)
    return b


def partitionWrap(i_lyst):
    ind, lyst = i_lyst
    if len(lyst) <= 1:
        return [lyst]
    b = partition(lyst, 0, len(lyst) - 1)
    return (ind, [lyst[:b], [lyst[b]], lyst[b + 1:]])


def quicksortParallel(lyst, n):
    numproc = 2 ** n
    # Basically, we're going to partition the list until it's all
    # singletons. We'll store each singleton in the master list.
    ml = list(lyst)

    pool = Pool(processes=numproc)
    results = [(0, lyst)]
    # the one initial argument to partitionWrap

    while len(results) > 0:
        # debug: print(str(results) + '\n\n\n')
        temp = pool.map(partitionWrap, results)
        # Each element of temp is a list of up to three lists.
        results = []
        for i, plist in temp:
            for ll in plist:  # for each little list in the partition output
                if len(ll) == 1:
                    ml[i] = ll[0]
                    i += 1
                elif len(ll) > 1:
                    results.append((i, ll))
                    i += len(ll)

    return ml


# Call the main method if run from the command line.
if __name__ == '__main__':
    main(sys.argv[1:])
