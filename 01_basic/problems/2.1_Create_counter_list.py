'''

Count the repetition of each element of a lst
'''

aList = [1, 2, 3, 4, 2, 3, 1, 4, 5, 6, 100, 100, 100]
D = dict()
D = D.fromkeys(aList, 0)

for i in aList:
    D[i] = D[i] + 1

print(D)