#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the balancedSums function below.
def balancedSums(arr):
    if len(arr) == 1:
        return "YES"
    else:
        right_sum = sum(arr)
        left_sum = 0
        num_ints = len(arr)

        for i in range(num_ints):
            current = arr[i]
            right_sum = right_sum-current
            if right_sum == left_sum:
                return "YES"
            left_sum += current
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
