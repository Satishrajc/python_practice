# 1: Below are the two lists convert it into the dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

print(dict(zip(keys, values)))

# ------------------------------------------------------- #

# 2. Merge following two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3 = {**dict1, **dict2}
dict2.update(dict1)
# or
# dict3 = dict1.copy()
# dict3.update(dict2)

print('dict2: ', dict2)
print('dict3: ', dict3)

# ------------------------------------------------------- #
# 3. Initialize dictionary with default values

employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}

resDict = dict.fromkeys(employees, defaults)
print(resDict)

# Individual data
print(resDict["Kelly"])

# ------------------------------------------------------- #
# 3. Get the key of a minimum value from the following dictionary
# Input:
# sampleDict = {
#     'Physics': 82,
#     'Math': 65,
#     'history': 75
# }

# Answer:
sampleDict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}
print(min(sampleDict, key=sampleDict.get))

# ------------------------------------------------------- #
