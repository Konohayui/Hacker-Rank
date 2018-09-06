import numpy as np

n, m = map(int, input().split(' '))

A = []
B = []

for _ in range(n):
    A.append([int(e) for e in input().split(' ')])

    
for _ in range(n):
    B.append([int(e) for e in input().split(' ')])
    
A, B = np.array(A), np.array(B)

print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)
print(A**B)
