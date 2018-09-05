import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    arr = arr[::-1]
    return numpy.array(arr, float)
    
arr = raw_input().strip().split(' ')
result = arrays(arr)
print(result)
