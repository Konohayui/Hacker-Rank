#!/bin/python3

"""
Time out for test cases 2, 3, and 4
"""

import math
import os
import random
import re
import sys
from itertools import combinations


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])

        result = 0
        com = combinations(list(range(1, n+1)), 2)
        for c in com:
            A, B = c[0], c[1]
            possible_val = A & B 
            if possible_val > result and possible_val < k:
                result = possible_val

        print(result)


"""
Jekus' solution

This solution works only if we know n and k
"""

T = int(input().strip())
for _ in range(T):
    n , k = map(int , input().split())
    print(k-1 if ((k-1) | k) <= n else k-2)
    
