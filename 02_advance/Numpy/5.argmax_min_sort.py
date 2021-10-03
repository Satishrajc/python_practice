import numpy as np

listArray = np.array([[1, 2, 3], [4, 5, 6], [6, 7, 8]])

# Finding index of max item value
listArray1 = np.array([1, 2, 3, 400, 5, 6])
print("index of max item value: ", listArray1.argmax())
print("index of min item value: ", listArray1.argmin())
print("sorting: ", listArray1.argsort())

print('-------')

listArray2 = np.array([[1, 2, 3], [4, 5, 6], [6, 10, 8]])
'''
[[1 2 3]
 [4 5 6]
 [6 7 8]]
''''''
[[1 2 3]
 [4 5 6]
 [6 10 8]]
'''
print("index of max item value: ", listArray2.argmax())
print("index of min item value: ", listArray2.argmin())

print("USING AXIS ")
print("index of max item value: ", listArray2.argmax(axis=0))
print("index of max item value: ", listArray2.argmax(axis=1))

print(listArray2.argsort(axis=0))
