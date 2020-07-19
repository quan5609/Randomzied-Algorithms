#!/usr/bin/env python3
import random
import numpy as np
import optparse
import os
import sys


def randomSearch(A, key):
    pivot = random.randint(0, len(A)-1)
    if A[pivot] == key:
        return pivot
    elif A[pivot] > key:
        return randomSearch(A[0:pivot], key)
    else:
        return randomSearch(A[pivot+1:len(A)], key)


def readCommand(argv):
    parser = optparse.OptionParser(
        description='Key')
    parser.add_option('--key',
                      dest='key',
                      default=1)
    (options, _) = parser.parse_args(argv)
    return options


if __name__ == "__main__":
    options = readCommand(sys.argv)
    A = [1, 2, 3, 4, 5, 6]
    key = int(options.key)
    print("Key found at index", randomSearch(A, key))
