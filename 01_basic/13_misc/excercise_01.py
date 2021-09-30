'''
Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
Write one line of Python that takes this list a and makes a new list that has only the even
elements of this list in it.
'''

# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# print([i for i in a if i%2 == 0])


'''
Reverse the words of sentence
Inupt:
  My name is Michele
Output:
  Michele is name My
'''

# s = 'My name is Michele'
# print(' '.join(s.split(' ')[::-1]))

'''
Program to print duplicates from a list of integers
Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
Output : output_list = [20, 30, -20, 60]
'''
# aDict = {}
# aList = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# dupList = []
# aDict = aDict.fromkeys(aList, 0)
#
# for i in aList:
#     if i in aDict.keys():
#         aDict[i] += 1
# print(aDict)
# print([key for key, value in aDict.items() if value > 1])

''''
Remove an empty tuple from a given list of tuples.

Input : tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), ('',''),()]
Output : [('ram', '15', '8'), ('laxman', 'sita'), ('krishna', 'akbar', '45'), ('', '')]
'''

# aList = [(), ('ram', '15', '8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), ('', ''), ()]
# print([i for i in aList if len(i) != 0])


'''
delete each element in the list which is divisible by 2 or all the even numbers. 
'''
# list1 = [11, 5, 17, 18, 23, 50]
#
# for index, item in enumerate(list1):
#     if item % 2 == 0:
#         list1.remove(item)
#
# print(list1)

'''

'''
