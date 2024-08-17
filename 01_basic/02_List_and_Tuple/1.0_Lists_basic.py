L1 = [1, 2, 3, 'a', 'b', 'a']  # Initial list

counter = 1
# Looping through the methods of list objects using dir() and printing non-magic methods
for i in dir(L1):
    if not i.ljust(8).startswith('__'):  # Filter out magic methods (those starting with '__')
        print(f"{counter}. list.{i}()")
        counter += 1

# Append 'c' to the end of the list
L1.append('c')
print('append   :', L1)  
# Output: append   : [1, 2, 3, 'a', 'b', 'a', 'c']

# Copying the list
L2 = L1.copy()
print('copy     :', L2)
# Output: copy     : [1, 2, 3, 'a', 'b', 'a', 'c']

# Counting the occurrences of 'a' in the list
print('count    :', L1.count('a'))
# Output: count    : 2  # 'a' appears twice in the list

# Extending the list by appending elements from another iterable
L1.extend([5, 6, 7])
print('extend   :', L1)
# Output: extend   : [1, 2, 3, 'a', 'b', 'a', 'c', 5, 6, 7]

# Finding the index of the first occurrence of 3 in the list
print('index    :', L1.index(3))
# Output: index    : 2

# Inserting 'QQQQQ' at index 5
L1.insert(5, "QQQQQ")
print('insert   :', L1)
# Output: insert   : [1, 2, 3, 'a', 'b', 'QQQQQ', 'a', 'c', 5, 6, 7]

# Removing and returning the item at index 2 (which is 3)
print('pop      :', L1.pop(2))
# Output: pop      : 3

# Printing the list after popping
print('pop      :', L1)
# Output: pop      : [1, 2, 'a', 'b', 'QQQQQ', 'a', 'c', 5, 6, 7]

# Removing the first occurrence of 'a' from the list
L1.remove('a')
print('remove   :', L1)
# Output: remove   : [1, 2, 'b', 'QQQQQ', 'a', 'c', 5, 6, 7]

# Reversing the list
L1.reverse()
print('reverse  :', L1)
# Output: reverse  : [7, 6, 5, 'c', 'a', 'QQQQQ', 'b', 2, 1]

# Sorting a new list L3 in ascending order
L3 = [3, 4, 56, 1]
L3.sort()
print('sort     :', L3)
# Output: sort     : [1, 3, 4, 56]

# Checking the type of L1 (should be a list)
print(type(L1))
# Output: <class 'list'>

# Finding the maximum value in a list
print(max([1, 2, 1, 200]))
# Output: 200

# Finding the minimum value in a list
print(min([1, 2, 1, 200]))
# Output: 1

# Getting the length of the list
print(len([1, 2, 1, 200]))
# Output: 4

# Converting a tuple into a list
print(list((1, 2, 3, 4)))
# Output: [1, 2, 3, 4]

# Summing the elements in a list
print(sum([1, 2, 1, 200]))
# Output: 204

print('\nSorted:')
# Sorting the list [1, 2, 1, 200] without modifying the original list
L4 = sorted([1, 2, 1, 200])
print(L4)
# Output: [1, 1, 2, 200]

print('Enumerate: ')
# Enumerating over L1, starting with index 2
for index, item in enumerate(L1, start=2):
    print(index, item)
# Output: 
# 2 7
# 3 6
# 4 5
# 5 c
# 6 a
# 7 QQQQQ
# 8 b
# 9 2
# 10 1

# Deleting the element at index 1 in L (which is 2)
L = [1, 2, 3]
del L[1]
print(L)
# Output: [1, 3]
