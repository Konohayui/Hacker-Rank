import numpy

n, m = map(int, input().split(' '))

arr = []
for _ in range(n):
    arr.append([int(e) for e in input().split(' ')])
    
arr = numpy.array(arr)

arr_min = numpy.min(arr, axis = 1)
arr_max = numpy.max(arr_min)

print(arr_max)
