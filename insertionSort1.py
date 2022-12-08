#!/bin/python3

import math
import os
import random
import re
import sys



def insertionSort1(n, arr):
    ele = arr[-1]
    arr[-1] = arr[-2]
    for i in range(n-1, 0, -1):
        if arr[i - 1] < ele:
            arr[i] = ele
            printArr(arr)
            break
        else:
            arr[i] = arr[i - 1]
            printArr(arr)
    if ele not in arr:
        arr[0] = ele
        printArr(arr)
    
            
def printArr(arr):
    for i in arr:
        print(i, end = " ")
    print()   
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
