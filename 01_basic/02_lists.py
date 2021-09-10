L1 = [1, 2, 3, 'a', 'b', 'a']

for i in (dir(L1)):
    print(f"print('{i.ljust(8)} :', L1.{i}())")

print('append   :', L1.append('c'))

L2 = L1.copy()
print('copy     :', L2)

print('count    :', L1.count('a'))

L1.extend([5, 6, 7])
print('extend   :', L1)

print('index    :', L1.index(3))  # Returns the first appearance of the specified value.

L1.insert(5, "QQQQQ")
print('insert   :', L1)

print('pop      :', L1.pop(2))  # Remove and return item at index (default last).
print('pop      :', L1)  # Raises IndexError if list is empty or index is out of range.

L1.remove('a')  # Remove first occurrence of value.
print('remove   :', L1)

L1.reverse()
print('reverse  :', L1)

L3 = [3, 4, 56, 1]
L3.sort()
print('sort     :', L3)

print(type(L1))  # It returns the class type of an object
print(max([1, 2, 1, 200]))  # It returns an item from the list with max value.
print(min([1, 2, 1, 200]))  # It returns an item from the list with min value.
print(len([1, 2, 1, 200]))  # It gives the total length of the list.
print(list((1, 2, 3, 4)))  # Converts a tuple into a list.
print(sum([1, 2, 1, 200]))

L4 = sorted([1, 2, 1, 200])
print(L4)

print(enumerate(L1))
