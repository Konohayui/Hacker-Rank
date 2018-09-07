import numpy as np

P = [float(e) for e in input().split()]
x = float(input())
y = np.polyval(P, x)

print(y)
