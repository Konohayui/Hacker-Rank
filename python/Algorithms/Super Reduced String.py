#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    if len(s) == 0:
        return "Empty String"
        
    else:
        s = list(s)
        n = len(s)
        i = 0
        
        while i < n - 1:
            if s[i] == s[i+1]:
                s = s[:i] + s[i+2:]
                i = 0
                n -= 2
                print(s)
                
            else:
                i += 1
        
        if len(s) == 0:
            return "Empty String"
            
        else:
            return "".join([e for e in s])
    
"""
Good Solution:
def superReducedString(s):
    res = []
    for c in s:
        if res and res[-1] == c:
            res.pop()
        else:
            res.append(c)
    res = ''.join(res)
    return res or "Empty String"
"""


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
