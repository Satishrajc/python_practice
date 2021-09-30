def foo():
    print("First statement")
    yield

    print("Second statement")
    yield


generator_object = foo()
next(generator_object)
next(generator_object)
