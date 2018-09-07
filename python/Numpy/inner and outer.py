import numpy as np

A =  np.array([int(e) for e in input().split(' ')])
B =  np.array([int(e) for e in input().split(' ')])

print(np.inner(A, B))
print(np.outer(A, B))
