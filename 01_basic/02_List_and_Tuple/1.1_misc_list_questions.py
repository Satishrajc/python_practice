# 1. Reverse a given list in Python without inbuilt functions

aList = [100, 200, 300, 400, 500]

# Reversing the list using slicing
reversed_list = aList[::-1]  # Creates a new reversed list using slicing
print(f"Reversed List using slicing: {reversed_list}")  # Output: [500, 400, 300, 200, 100]

# Reversing the list using a manual loop (no inbuilt reverse() method)
manual_reverse = []
for i in range(len(aList) - 1, -1, -1):  # Iterating from the end to the start of the list
    manual_reverse.append(aList[i])

print(f"Reversed List using manual loop: {manual_reverse}")  # Output: [500, 400, 300, 200, 100]


# ------------------------------------------------------- #

# 2. Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

# Expected output: ['My', 'name', 'is', 'Kelly']
con_list = []
for i in zip(list1, list2):  # Zip combines the two lists element-wise
    con_list.append(i[0] + i[1])  # Concatenate the corresponding elements

# Alternatively, using list comprehension: con_list = [i + j for i, j in zip(list1, list2)]
print(f'Concatenated List: {con_list}')  # Output: ['My', 'name', 'is', 'Kelly']


# ------------------------------------------------------- #

# 3. Given a Python list of numbers, turn every item of the list into its square

aList = [1, 2, 3, 4, 5, 6, 7]

# Using list comprehension to square each element
squared_list = [i * i for i in aList]
print(f'Squared List: {squared_list}')  # Output: [1, 4, 9, 16, 25, 36, 49]


# ------------------------------------------------------- #

# 4. Concatenate two lists in the following order

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

# Expected output: ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
output = []
for item in list1:
    for data in list2:
        output.append(item + data)  # Concatenate each element from list1 with each element from list2

# Alternatively, using list comprehension: output = [x + y for x in list1 for y in list2]
print(f"Concatenated Lists: {output}")  # Output: ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

# ------------------------------------------------------- #
