import numpy as np

listArray = np.array([[1, 2, 3], [4, 5, 6], [6, 7, 8]])
'''
print(listArray):

[[ 1  2  3]
 [ 4  5  6]
 [ 6  7  8]
'''
# Axis 0 : Row
print(listArray.sum(axis=0))

# Axis 0 : Column
print(listArray.sum(axis=1))
