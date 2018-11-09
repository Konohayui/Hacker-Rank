#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternate function below.
from itertools import combinations

def alternate(s):
    chars = list(set(s))
    n_char = len(chars)
    longest = 0

    if n_char < 2:
        return longest
        
    combs = combinations(chars, n_char-2)

    for comb in list(combs):
        temp = s
        for c in comb:
            temp = temp.replace(c, "")

        s_len = len(temp)
        count = 0
        for i in range(s_len-1):
            if temp[i] == temp[i+1]:
                count += 1
    
        if count == 0:
            longest = max(longest, len(temp))
        
    return longest

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
