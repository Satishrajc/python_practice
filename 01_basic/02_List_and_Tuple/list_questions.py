# 1. Reverse a given list in Python without inbuilt functions
aList = [100, 200, 300, 400, 500]

print(aList[::-1])

aList.reverse()
print(aList)

# ------------------------------------------------------- #
# 2. Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

# Expected output: ['My', 'name', 'is', 'Kelly']
con_list = []
for i in zip(list1, list2):
    con_list.append(i[0] + i[1])

# con_list = [i + j for i, j in zip(list1, list2)]
print(f'con_list: {con_list}')

# ------------------------------------------------------- #
# 3. Given a Python list of numbers. Turn every item of a list into its square
aList = [1, 2, 3, 4, 5, 6, 7]
print([i * i for i in aList])

# ------------------------------------------------------- #
# 4. Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

# Expected output: ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
output = []
for item in list1:
    for data in list2:
        output.append(item + data)

# output = [x+y for x in list1 for y in list2]
print(f"output: ", output)

# ------------------------------------------------------- #
