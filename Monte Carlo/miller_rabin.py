#!/usr/bin/env python3
import random
import numpy as np
import optparse
import os
import sys


def power(x, y, p):
    res = 1
    x = x % p
    while (y > 0):
        if (y & 1):
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res


def millerRabinTest(n):
    if (n <= 1 or n == 4):
        return False
    if (n <= 3):
        return True
    d = n - 1
    while (d % 2 == 0):
        d //= 2
    a = 2 + random.randint(1, n - 4)
    x = power(a, d, n)
    if (x == 1 or x == n - 1):
        return True
    while (d != n - 1):
        x = (x * x) % n
        d *= 2
        if (x == 1):
            return False
        if (x == n - 1):
            return True
    return False


def readCommand(argv):
    parser = optparse.OptionParser(
        description='Number of trials')
    parser.add_option('--input',
                      dest='input',
                      default=31)
    parser.add_option('--trials',
                      dest='trials',
                      default=10)
    (options, _) = parser.parse_args(argv)
    return options


def main():
    options = readCommand(sys.argv)
    n = int(options.input)
    trials = int(options.trials)
    for _ in range(trials):
        if not millerRabinTest(n):
            return "Composite"
    return "Probably Prime"


if __name__ == "__main__":
    print(main())
