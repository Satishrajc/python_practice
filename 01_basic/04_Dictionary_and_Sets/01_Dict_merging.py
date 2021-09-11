# code
# Python code to merge dict using a single 
# Python >= 3.9
# def Merge(dict1, dict2):
#     res = dict1 | dict2
#     return res
#
#
# # Driver code
# dict1 = {'x': 10, 'y': 8}
# dict2 = {'a': 6, 'b': 4}
# dict3 = Merge(dict1, dict2)
# print(dict3)


# -----------------------------

# Python >= 3.8

# Driver code
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

# This return None
# dict2.update(dict1)
dict2 = {**dict1, **dict2}
# changes made in dict2
print(dict2)
