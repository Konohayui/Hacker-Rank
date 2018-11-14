#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    missinges = []
    second = Counter(arr)
    orginal = Counter(brr)

    for num in orginal.keys():
        if num in second.keys():
            if orginal[num] > second[num]:
                missinges.append(num)
        else:
            missinges.append(num)

    return sorted(missinges)
            

"""
without using Counter

def missingNumbers(arr, brr):
    largest = max(max(arr), max(brr)) + 1
    table = [0]*largest
    
    for a in arr:
        table[a] += 1 
        
    for b in brr:
        table[b] -= 1 
        
    return [num for num in range(largest) if table[num] != 0]

"""


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
