#!/usr/bin/env python3
import random
import numpy as np
import optparse
import os
import sys


def freivalds(A, B, C):
    r = np.random.randint(0, 2, size=(2))
    P = np.dot(A, np.dot(B, r)) - np.dot(C, r)
    print(P)
    if not np.any(P):
        return True
    return False


def readCommand(argv):
    parser = optparse.OptionParser(
        description='Number of trials')
    parser.add_option('--trials',
                      dest='trials',
                      default=5)
    (options, _) = parser.parse_args(argv)
    return options


def printMat(mat):
    print(mat)


def main():
    A = np.random.randint(0, 5, size=(2, 2))
    B = np.random.randint(0, 5, size=(2, 2))
    C = np.random.randint(0, 5, size=(2, 2))
    options = readCommand(sys.argv)
    [printMat(mat)for mat in [A, B, C]]
    trials = int(options.trials)
    for _ in range(trials):
        if not freivalds(A, B, C):
            return "C != AxB"
    return "C probably == AxB"


if __name__ == "__main__":
    print(main())
