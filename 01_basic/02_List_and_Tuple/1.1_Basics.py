import copy

# Normal assignment using reference (bList = aList)
print('\nNormal Assignment:')
aList = [1, 2, 3, [6, 7, 8]]
bList = aList  # bList is now a reference to aList (both point to the same object in memory)
bList.append(100)  # Changes in bList will reflect in aList

print("aList: ", aList)  # Output: [1, 2, 3, [6, 7, 8], 100]
print("bList: ", bList)  # Output: [1, 2, 3, [6, 7, 8], 100]

# Slicing (creates a shallow copy of the outer list)
print('\nSlicing:')
aList = [1, 2, 3, [6, 7, 8]]
bList = aList[:]  # Shallow copy (only the outer list is copied, nested lists are not)
bList.append(100)

print("aList: ", aList)  # Output: [1, 2, 3, [6, 7, 8]]
print("bList: ", bList)  # Output: [1, 2, 3, [6, 7, 8], 100]

# Shallow copy using .copy() method (also works similarly to slicing)
print('\nShallow Copy:')
aList = [1, 2, 3, [6, 7, 8]]
bList = aList.copy()  # Shallow copy (only the outer list is copied)
# Alternatively: bList = copy.copy(aList) or bList = aList[:]
bList.append(100)

print("aList: ", aList)  # Output: [1, 2, 3, [6, 7, 8]]
print("bList: ", bList)  # Output: [1, 2, 3, [6, 7, 8], 100]

print('BUT..')
bList[3][0] = 200  # Modifying the nested list affects both aList and bList because they share the same nested list reference

print("aList: ", aList)  # Output: [1, 2, 3, [200, 7, 8]]
print("bList: ", bList)  # Output: [1, 2, 3, [200, 7, 8], 100]

# Deep copy (creates a completely independent copy of the list and all nested elements)
print('\nDeep Copy:')
aList = [1, 2, 3, [6, 7, 8]]
bList = copy.deepcopy(aList)  # Deep copy (copies everything, including nested lists)
bList[3][0] = 300  # Modifying the nested list only affects bList

print("aList: ", aList)  # Output: [1, 2, 3, [6, 7, 8]] (unchanged)
print("bList: ", bList)  # Output: [1, 2, 3, [300, 7, 8]] (only bList changes)
