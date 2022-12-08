#!/bin/python3

import math
import os
import random
import re
import sys


def countingSort(arr):
    freqArr = []
    for i in range(100):
        freqArr.append(0)
    for i in arr:
        freqArr[i] += 1
    return freqArr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
