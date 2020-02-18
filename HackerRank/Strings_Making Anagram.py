#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.


def makeAnagram(a, b):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    total = 0
    for letter in alphabet:
        findInA = a.count(letter)  # 3 0 1 1
        findInB = b.count(letter)  # 1 1 2 3

        total += abs(findInA - findInB)
        # total = +2 -1 + 1

    return total

    # 오답, 공통으로 존재하는 철자를 없애고 남은 철자의 개수를 더하자
    # count = 0

    # for i in range(26):
    #     checkA = a.find(alphabet[i])
    #     checkB = a.find(alphabet[i])

    #     if checkA and checkB is not -1:
    #         count += 1

    # value = len(a) + len(b) - count*2
    # return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()
    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
