def decorator_outside(message):
    def decorator_inside(f):
        def wrapper_foo(a, b):
            print(message)
            print('Before foo called')
            f(a, b)
            print('After foo called')

        return wrapper_foo

    # Note: sending 'decorator_inside' return
    return decorator_inside


@decorator_outside("Argument to decorator")
def foo(a, b):
    print("Inside Foo")


foo(10, 20)
