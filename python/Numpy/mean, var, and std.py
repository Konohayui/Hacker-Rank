import numpy
numpy.set_printoptions(legacy = '1.13')

n, m = map(int, input().split(' '))
arr = []

for _ in range(n):
    arr.append([int(e) for e in input().split(' ')])

arr = numpy.array(arr)
print(numpy.mean(arr, axis = 1))
print(numpy.var(arr, axis = 0))
print(numpy.std(arr))
