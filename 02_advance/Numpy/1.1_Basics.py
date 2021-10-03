import numpy as np

# Defining specific size of numpy array
# n = np.array([1, 2, 3], numpy.int8)


listArray = np.array([[1, 2, 3], [4, 5, 6], [6, 7, 8]])

# print('listArray: ', listArray)
#
# print('listArray.shape: ', listArray.shape)
# print('listArray.dtype: ', listArray.dtype)
# print('listArray.size: ', listArray.size)

arg = np.arange(15)
# print('arange: ', arg)

linSpace = np.linspace(1, 10, 20)
# print('linSpace: ,', linSpace)


zero = np.zeros((2, 5))
# print('zero: ,', zero)
# print('zero dtype: ,', zero.dtype)


# Creating random elements
empt = np.empty((4, 6))
# print('empt: ,', empt)


# Creating identity metric
identity_array = np.identity(10)
# print('identity: ,', identity_array)


# Reshaping the existing elements
listArray = np.array([[1, 2, 3], [4, 5, 6], [6, 7, 8], [9, 10, 11]])
# print('listArray: ', listArray)
# print('Reshaping listArray: ', listArray.reshape(6,2))

# Multi array to 1D array conversion
listArray = np.array([[1, 2, 3], [4, 5, 6], [6, 7, 8], [9, 10, 11]])
# print('listArray: ', listArray)
# print('ravel 1D listArray: ', listArray.ravel())

# Finding dimensions of array
listArray = np.array([[[1, 2, 3], [4, 5, 6]], [[6, 7, 8], [9, 10, 11]]])
# print("Dimension: ", listArray.ndim)
# print(listArray[1][1])

# Finding bytes consumed by array
listArray = np.array([[1, 2, 3], [4, 5, 6], [6, 7, 8]])
# print("bytes: ", listArray.nbytes)

# Finding index of max item value
listArray1 = np.array([1, 2, 3, 400, 5, 6])
# print("index of max item value: ", listArray1.argmax())
# print("index of min item value: ", listArray1.argmin())
# print("sorting: ", listArray1.argsort())


listArray1 = np.array([1, 2, 3, 400, 5, 6])
print('sqrt: ', np.sqrt(listArray1))
print('max: ', np.max(listArray1))
print('min: ', np.min(listArray1))
print('sum: ', np.sum(listArray1))


listArray2 = np.array([[1, 2, 3], [4, 5, 6], [6, 7, 8], [9, 10, 11]])
print(np.where(listArray2 > 10))