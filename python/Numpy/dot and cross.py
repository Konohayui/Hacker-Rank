import numpy as np

n = int(input())

A =  np.array([[int(e) for e in input().split(' ')] for _ in range(n)])
B =  np.array([[int(e) for e in input().split(' ')] for _ in range(n)])

print(np.dot(A, B))
