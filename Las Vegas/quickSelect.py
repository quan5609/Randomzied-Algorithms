#!/usr/bin/env python3
import random
import numpy as np
import optparse
import os
import sys


def quickSelect(arr, start, stop, order):
    # print(arr[start: stop+1])
    if start == stop:
        return arr[start]
    pivotindex = partitionrand(arr, start, stop)
    k = pivotindex+1
    if k == order:
        return arr[k-1]
    elif order < k:
        return quickSelect(arr, start, pivotindex - 1, order)
    else:
        return quickSelect(arr, pivotindex + 1, stop, order)


def partitionrand(arr, start, stop):
    randpivot = random.randrange(start, stop)
    arr[start], arr[randpivot] = arr[randpivot], arr[start]
    return partition(arr, start, stop)


def partition(arr, start, stop):
    pivot = start
    i = start + 1
    for j in range(start + 1, stop + 1):
        if arr[j] <= arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
    arr[pivot], arr[i - 1] = arr[i - 1], arr[pivot]
    pivot = i - 1
    return pivot


def readCommand(argv):
    parser = optparse.OptionParser(
        description='Order to find')
    parser.add_option('--order',
                      dest='order',
                      default=4)
    (options, _) = parser.parse_args(argv)
    return options


if __name__ == "__main__":
    options = readCommand(sys.argv)
    order = int(options.order)
    A = [1, 4, 3, 2, 6, 5]
    print("Array:", A)
    print("The %d th smallest in array is %d" %
          (order, quickSelect(A, 0, len(A)-1, order)))
