import numpy as np

A = np.array([[float(e) for e in input().split(' ')] for _ in range(int(input()))])
print(round(np.linalg.det(A), 2))
