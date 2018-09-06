'''
there is a bug that shifts intergers by 1 space in test cases
'''

import numpy

n, m = map(int, input().split(' '))
print(str(numpy.eye(n, m)).replace('1',' 1').replace('0',' 0'))

