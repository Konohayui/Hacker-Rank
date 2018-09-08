#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        
    maximum = -100
    
    m, n = len(arr), len(arr[0])
    for i in range(m-2):
        for j in range(n-2):
            sum_glass = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            sum_glass += arr[i+1][j+1]
            sum_glass += arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            
            maximum = max(maximum, sum_glass)
            
    print(maximum)
