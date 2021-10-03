'''

Count the repetition of each element of a string
'''

aString = 'absbsbabaiawabaccacac'

counter = dict()
counter = counter.fromkeys(list(aString), 0)

for s in aString:
    counter[s] = counter[s] + 1

print(counter)
