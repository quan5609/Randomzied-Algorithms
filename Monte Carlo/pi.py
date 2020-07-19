#!/usr/bin/env python3
import random
import numpy as np
import optparse
import os
import sys

def piMonteCarlo(maxPoint):
    innerPoints = 0
    for _ in range(maxPoint):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        if np.square(x) + np.square(y) <= 1:
            innerPoints += 1
    return 4*innerPoints/maxPoint

def readCommand(argv):
    parser = optparse.OptionParser(
        description='Number of trials')              
    parser.add_option('--trials',
                      dest='trials',
                      default=1000000)
    (options, _) = parser.parse_args(argv)
    return options

if __name__ == "__main__":
    options = readCommand(sys.argv)
    print("Pi:",piMonteCarlo(int(options.trials)))