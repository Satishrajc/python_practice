

class DecoratorClass:
    def __init__(self, func):
        # Note that here 'func' represents 'foo'
        print("Inside __init__")
        self.func = func

    def __call__(self, a, b):
        print("Inside __call__")
        self.func(a, b)


@DecoratorClass
def foo(a, b):
    print("Inside Foo")


foo(10, 20)