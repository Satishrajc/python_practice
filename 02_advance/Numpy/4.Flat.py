import numpy as np

listArray = np.array([[1, 2, 3], [4, 5, 6], [6, 7, 8]])


flat_array = listArray.flat

for item in flat_array:
    print(item)


