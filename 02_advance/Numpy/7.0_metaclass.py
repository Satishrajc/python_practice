# **Metaclasses:**
# In Python, metaclasses are a powerful feature that allows you to customize the behavior of class creation. 
# In Python, everything is an object, including classes themselves. Metaclasses are the "class of a class,
# " meaning they define how classes are created, just as classes define how objects are created.

# To create a custom metaclass, you can define a new class that inherits from `type`. 
# The `type` is the default metaclass in Python, responsible for creating all classes. 
# You can override the `__new__` or `__init__` methods in your custom metaclass to 
# customize the class creation process.

#  The __init__ method of a metaclass typically receives the following default attributes:

# cls (the metaclass itself): This is the first argument passed to the __init__ method of the metaclass. It represents the metaclass itself, not an instance of the class being created.

# name (str): The name of the class being created. It is a string representing the name of the class.

# bases (tuple): A tuple containing the base classes of the class being created. These base classes represent the class's inheritance hierarchy.

# attrs (dict): A dictionary containing the attributes and methods defined in the class. The keys are the attribute/method names, and the values are the corresponding attribute/method objects.

class MyMeta(type):
    def __init__(cls, name, bases, attrs):
        print("Metaclass __init__ called.")
        print("Metaclass:", cls)
        print("Class Name:", name)
        print("Base Classes:", bases)
        print("Attributes:", attrs)
        # Add a prefix "My" to all attributes in the class
        prefixed_attrs = {f"My_{key}": value for key, value in attrs.items()}
        print(prefixed_attrs)
        super().__init__(name, bases, prefixed_attrs)

class MyClass(metaclass=MyMeta):
    x = 10
    y = 20

obj = MyClass()
print(obj.My_x)  # Output: 10
print(obj.My_y)  # Output: 20

# In this example, we define a custom metaclass `MyMeta`, which prefixes all 
# attributes of the class `MyClass` with "My_". So, when we create an instance of `MyClass`, 
# the attributes `x` and `y` are automatically transformed into `My_x` and `My_y`, respectively.

# If you have any questions or need further clarification, feel free to ask. Now, 
# let's move on to the next advanced-level question.