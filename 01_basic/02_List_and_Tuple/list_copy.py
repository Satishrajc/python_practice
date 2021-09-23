'''
Note:
bList = aList --> Will chnage if both the list if any one list changes
bList = aList[] or aList.copy() or copy.copy(aList)  --> Changes will happen for nested lists
bList = copy.deepcopy(aList) --> Creates separate memory address
'''

import copy

print('\nNormal:')
aList = [1, 2, 3, [6, 7, 8]]
bList = aList
bList.append(100)

print("aList: ", aList)
print("bList: ", bList)

print('\nSlicing:')
aList = [1, 2, 3, [6, 7, 8]]
bList = aList
bList.append(100)

print("aList: ", aList)
print("bList: ", bList)

print('\nshallow copy:')
aList = [1, 2, 3, [6, 7, 8]]
bList = aList.copy()
# bList = copy.copy(aList)
# bList = aList[:]
bList.append(100)

print("aList: ", aList)
print("bList: ", bList)

print('BUT..')
bList[3][0] = 200
print("aList: ", aList)
print("bList: ", bList)

print('\ndeep copy:')
aList = [1, 2, 3, [6, 7, 8]]
bList = copy.deepcopy(aList)
bList[3][0] = 300

print("aList: ", aList)
print("bList: ", bList)
