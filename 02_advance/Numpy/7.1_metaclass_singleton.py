
# **Metaclasses Example: Singleton**
# One common use case of metaclasses is to implement the Singleton design pattern. A Singleton class ensures that only one instance of the class can ever exist. Every time you try to create a new instance, it will return the same instance that was created earlier.

# Here's how you can implement a Singleton using a custom metaclass:

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class SingletonClass(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

# Creating instances of SingletonClass
instance1 = SingletonClass(10)
instance2 = SingletonClass(20)

# Both instances point to the same object
print(instance1 is instance2)  # Output: True
print(instance1.value)  # Output: 10
print(instance2.value)  # Output: 10


# In this example, we define a custom metaclass `SingletonMeta`. The `__call__` method in 
# the metaclass gets invoked every time an instance of the class is created. It checks 
# whether an instance of the class already exists in the `_instances` dictionary. If it does, 
# it returns the existing instance; otherwise, it creates a new instance and stores it in the dictionary.

# When we create instances of `SingletonClass`, even though we pass different values during 
# initialization, the instances will always refer to the same object. This ensures that only 
# one instance of `SingletonClass` exists throughout the program's execution.

# This is just one of the many use cases of metaclasses. They provide a powerful way to 
# control class creation and can be used to implement various design patterns and enforce 
# coding conventions.

# If you have any more questions or need further examples, feel free to ask!