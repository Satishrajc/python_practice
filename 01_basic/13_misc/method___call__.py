class MyClass:

    def __init__(self):
        print("Calle __init__")

    def __str__(self):
        return "Calle __str__"

    def __call__(self):
        print("Calle __call__")


# __init__ will execute
obj = MyClass()

# __str__ will execute
print(obj)

# __call__ will execute also can send parameters
obj()
