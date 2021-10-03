print("EVAL : ")
print("Eval: ", eval('3 + 4'))

print('-' * 20)
print('ANY: ')
print("any mixed boolean: ", any([False, True, False, False]))
print("any all True: ", any([True, True, True, True]))
print("any all False: ", any([False, False, False, False]))

print('-' * 20)
print('ALL: ')
print("all mixed boolean: ", all([False, True, False, False]))
print("all True: ", all([True, True, True, True]))
print("all False: ", all([False, False, False, False]))

print('-' * 20)
print('LAMBDA: ')
# lambda arguments : expression
aList = [1, 2, 3, 4, 5]
bList = [6, 7, 8, 9, 10]

aDict = lambda aList, bList: zip(aList, bList)
print(dict(aDict(aList, bList)))

print('-' * 20)
print('MAP: ')
# map(function, iterator)
print(list(map(lambda x: x * x, [1, 2, 3, 4])))

print('-' * 20)
print('FILTER: ')
# filter(function, Expression) --> only outputs True calues
seq = [0, 1, 2, 3, 5, 8, 13]

# result contains odd numbers of the list
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))

# result contains even numbers of the list
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))


set("param", [1,2,3,3])
