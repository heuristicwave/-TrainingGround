#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.


def rotLeft(a, d):
    rotation = d
    element = a
    size = len(element)

    # Your code did not execute within the time limits
    # tmp = 0

    # for i in range(rotation):
    #     tmp = element[0]

    #     for j in range(size):
    #         if j+1 <size:
    #             element[j] = element[j+1]

    #     element[size-1] = tmp

    for i in range(rotation):
        f = element[0]
        element.remove(f)
        element.append(f)

    return element


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
