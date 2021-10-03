
# From Python3 tuple compression is act as  generators (and not list comprehension)
tuple_result = (i * i for i in range(10))
for i in tuple_result:
    print(i, end=' ')

list_result = [i * i for i in range(10)]

print()
print(type(tuple_result))
print(type(list_result))
'''
Hence tuple is efficient than list due to this nature 
'''

