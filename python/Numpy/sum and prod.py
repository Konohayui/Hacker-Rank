import numpy

n, m = map(int, input().split(' '))

arr = []
for _ in range(n):
    arr.append([int(e) for e in input().split(' ')])
    
arr = numpy.array(arr)

s = numpy.sum(arr, axis = 0)
# print(s)
p = numpy.prod(s, axis = None)
print(p)
