import numpy

n, m = input().split()
n, m = int(n), int(m)

arr = []
for _ in range(n):
    arr.append([int(e) for e in input().split()])
    
arr = numpy.array(arr)
print(numpy.transpose(arr))
print(arr.flatten())

