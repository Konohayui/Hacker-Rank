#!/bin/python3

import math
import os
import random
import re
import sys

def is_weird(n):
    if n % 2 == 0:
        if 2 <= n <= 5:
            print("Not Weird")
        elif 5 <= n <= 20:
            print("Weird")
        else:
            print("Not Weird")
    else:
        print("Weird")
    
if __name__ == '__main__':
    N = int(input())
    is_weird(N)
