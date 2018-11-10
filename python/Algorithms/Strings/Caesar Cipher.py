#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
# ascii A-Z:65-90 && a-z:97-122
def caesarCipher(s, k):
    if len(s) == 0:
        return ""
        
    new_string = []
    for i in range(len(s)):
        if 97 <= ord(s[i]) <= 122:
            new_string.append(chr(((ord(s[i])-97+k)%26)+97))
        elif 65 <= ord(s[i]) <= 90:
            new_string.append(chr(((ord(s[i])-65+k)%26)+65))
        else:
            new_string.append(s[i])
    return "".join(new_string)
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
