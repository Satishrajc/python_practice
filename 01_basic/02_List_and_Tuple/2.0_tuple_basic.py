T1 = (1, 2, 3, 'a', 'b', 'a')

counter = 1
for i in (dir(T1)):
    if not i.ljust(8).startswith('__'):
        print(f"{counter}. tuple.{i}()")
        counter += 1
