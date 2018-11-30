#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the weightedUniformStrings function below.    
def weightedUniformStrings(s, queries):
    prev = s[0]
    w = ord(prev) - 96
    weights = {w:0}
    
    for i, l in enumerate(s[1:]):
        if prev == l:
            w += ord(l) - 96
            weights[w] = 0
        else:
            w = ord(l) - 96
            weights[w] = 0
        
        prev = l 
    return ["Yes" if q in weights else "No" for q in queries]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
