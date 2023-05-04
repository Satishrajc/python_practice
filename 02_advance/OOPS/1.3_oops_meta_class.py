"""
In Python, a metaclass is a class that defines the behavior of other classes. 
It is used to control the creation of classes, much like classes control the creation of instances.

In this example, MyMeta is the metaclass that defines the behavior of MyClass. 
When we define MyClass with metaclass=MyMeta, Python automatically calls the 
__new__ method of MyMeta with arguments MyClass, a tuple of base classes, and 
a dictionary of class attributes.

In the __new__ method of MyMeta, we can modify the dictionary of attributes as we like. 
In this case, we add two class attributes, class_name and class_variables, to the attrs 
dictionary. We then call super().__new__ with the same arguments, which creates and 
returns the new class object with the modified attributes.

Finally, when we access the class_name and class_variables attributes of MyClass, 
they have the values we set in the MyMeta metaclass. Note that MyMeta can define 
any behavior we want for MyClass, and we can define multiple metaclasses to apply 
different behaviors to different classes.
"""


class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        print("In __new__")
        print(f" name: {name}, bases: {bases}, attrs: {attrs}")
        attrs["class_name"] = name
        attrs["class_variables"] = {}
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=MyMeta):
    pass

"""
Run the code without creating object - output: in __new__
__new__ will be called even before creating the object

The parameters will be automatically passed to Meta class
"""
print(MyClass.class_name)  # output: MyClass
print(MyClass.class_variables)  # output: {}
