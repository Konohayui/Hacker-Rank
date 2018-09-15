import numpy as np, math
from scipy.stats import mode

n = int(input())

array = [int(i) for i in input().strip().split( )]

print(np.mean(array))
print(np.median(array))
print(int(mode(array)[0]))
