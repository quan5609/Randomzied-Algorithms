#!/usr/bin/env python3
import random
import numpy as np
import optparse
import os
import sys


def quicksort(arr, start, stop):
    if(start < stop):
        pivotindex = partitionrand(arr, start, stop)
        quicksort(arr, start, pivotindex)
        quicksort(arr, pivotindex + 1, stop)
    return arr


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
        description='Number of trials')
    parser.add_option('--trials',
                      dest='trials',
                      default=1000000)
    (options, _) = parser.parse_args(argv)
    return options


if __name__ == "__main__":
    A = [1, 4, 3, 2, 6, 5]
    print("Array:", A)
    print("Sorted Array:", quicksort(A, 0, len(A)-1))
