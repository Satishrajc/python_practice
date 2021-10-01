from multipledispatch import dispatch

# ----------------------------------------- #
print('-' * 20, '\nMethod 1: ')


def add(arg1, arg2, arg3=10):
    print(sum([arg1, arg2, arg3]))


add(1, 2)
add(1, 2, 3)

# ----------------------------------------- #

print('-' * 20, '\nMethod 2: ')


def add(*arg1):
    print(sum(arg1))


add(1, 3)
add(1, 2, 3)

# ----------------------------------------- #
print('-' * 20, '\nMethod 3: Most efficient')
print('''In Backend, Dispatcher creates an object which stores different implementation and 
on runtime, it selects the appropriate method as the type and number of parameters passed.''')

@dispatch(int, int)
def add(arg1, arg2):
    print(sum([arg1, arg2]))


@dispatch(int, int, int)
def add(arg1, arg2, arg3):
    print(sum([arg1, arg2, arg3]))


add(1, 2)
add(1, 2, 3)

