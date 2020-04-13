# Sorting, time complexity under O(n)
# Counting Sort Algorithm

import sys

n = int(sys.stdin.readline())   # for read large data
array = [0] * 10001

for i in range(n):
    data = int(sys.stdin.readline())
    array[data] += 1

for i in range(10001):
    if array[i] != 0:
        for j in range(array[i]):
            print(i)
