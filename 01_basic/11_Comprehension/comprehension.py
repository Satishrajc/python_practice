L1 = [n for n in range(10)]
print("L1 : ", L1)

# Both are same
L2 = [n for n in range(10) if n % 2 == 0]
L3 = filter(lambda n: n % 2 == 0, range(10))
print("L2: ", L2)
for i in L3:
    print(i)

L4 = [n * n for n in range(10)]
L5 = map(lambda n: n * n, range(10))
print("L4 : ", L4)
for i in L5:
    print(i)

# Loop inside a loop
L6 = [(n, i) for n in 'ab' for i in "123"]
print("L6 : ", L6)

# ----------------------------------------------------------------

D = {k: v for k in 'abcd' for v in '1234'}
print('D : ', D)

# ----------------------------------------------------------------

S = {n for n in range(10)}
print("S: ", S)
