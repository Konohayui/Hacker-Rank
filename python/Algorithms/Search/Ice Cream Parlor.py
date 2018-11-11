#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):
    flavor_map = {}
    for i1 in range(len(arr)):
        ice1 = arr[i1]
        ice2 = m - ice1
        if ice2 in flavor_map:
            i2 = arr.index(ice2)
            return sorted([i1+1, i2+1])
        if not ice1 in flavor_map:
            flavor_map[ice1] = i1 
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
