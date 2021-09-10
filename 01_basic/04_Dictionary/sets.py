s1 = {1, 2, 3, 'a', 'b', 1, 1}

counter = 1
for i in (dir(s1)):
    if not i.ljust(8).startswith('__'):
        print(f"{counter}. {i}()")
        counter += 1

s = set()

s2 = {1, 2, 3, 'a', 5, 6}

# for i in dir(s1):
# 	print(i)

print("copy                        : ", s1.copy())
print("difference                  : ", s1.difference(s2))
# print("difference_update           : ", s1.difference_update(s2 ))
# print("discard                     : ", s1.discard( ))
print("intersection                : ", s1.intersection(s2))
# print("intersection_update         : ", s1.intersection_update( ))
# print("isdisjoint                  : ", s1.isdisjoint( ))
# print("issubset                    : ", s1.issubset( ))
# print("issuperset                  : ", s1.issuperset( ))
# print("pop                         : ", s1.pop( ))

# print("symmetric_difference        : ", s1.symmetric_difference( ))
# print("symmetric_difference_update : ", s1.symmetric_difference_update( ))

print("union                       : ", s1.union(s2))

s1.update(s2)
print("update						:", s1)

s1.remove(1)
print("remove                      : ", s1)

s1.clear()
print("clear                       : ", s1)
