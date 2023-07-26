class MyMeta(type):
    def __init__(cls, name, bases, attrs):
        # Add a prefix "My_" to all attributes in the class
        prefixed_attrs = {f"My_{key}": value for key, value in attrs.items()}
        for key, value in prefixed_attrs.items():
            setattr(cls, key, value)
        super().__init__(name, bases, attrs)

class MyClass(metaclass=MyMeta):
    x = 10
    y = 20

obj = MyClass()
print(obj.My_x)  # Output: 10
print(obj.My_y)  # Output: 20
