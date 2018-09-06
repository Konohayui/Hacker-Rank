import numpy as np
np.set_printoptions(sign = ' ')

arr = []
arr.append([e for e in input().strip().split(' ')])

arr = np.array(arr, dtype = float)

print(*np.floor(arr))
print(*np.ceil(arr))
print(*np.rint(arr))

