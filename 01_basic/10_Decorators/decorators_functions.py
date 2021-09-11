def decorator_function(f):
    # Decorators takes function name as argument: here f --> foo
    def wrapper_foo(a, b):
        print('Before foo called')
        f(a, b)
        print('Before foo called')

    return wrapper_foo


@decorator_function
def foo(a, b):
    print("Inside Foo")


foo(10, 20)
