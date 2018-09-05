import numpy

arr = raw_input().strip().split(' ')
arr = numpy.array(arr, int)
new_arr = numpy.reshape(arr, (3, 3))
print(new_arr)



