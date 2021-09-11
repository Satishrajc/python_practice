

# Generators using list comprehension
# From Python3 tuple compression is act as  generators
result = (i * i for i in range(10))
for i in result:
    print(i, end=' ')

res = [i * i for i in range(10)]

print()
print(type(result))
print(type(res))

