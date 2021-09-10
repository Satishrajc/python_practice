import copy

L1 = [1, 2, 3, 'a', 'b', 'a']

for i in (dir(L1)):
    print(f"print('{i.ljust(8)} :', L1.{i}())")

L1 = [1, 2, 3]
L2 = [4, 5, 6, [6, 7]]

L1 = copy.deepcopy(L2)

print(L1)
L1[3][0] = 100
print(L2)
