'''
In Python, both @classmethod and @staticmethod are used to define methods 
that belong to a class rather than to an instance of the class. However, 
there is a subtle difference between the two.

@classmethod is used to define a method that is bound to the class and not 
the instance of the class. The method can access and modify the class state 
that applies to all instances of the class. It takes the class as the first argument, 
which is usually called cls.

Here's an example of @classmethod:

* The class method can only access the class attributes but not the instance attributes.
* The class method can be called using ClassName.MethodName() and also using object.
* It can return an object of the class.

When to use what?
We generally use class method to create factory methods. Factory methods return class objects ( similar to a constructor ) for different use cases.
We generally use static methods to create utility functions.
'''

class MyClass:
    class_variable = 0

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @classmethod
    def class_method(cls, num):
        cls.class_variable += num

my_obj1 = MyClass(10)
my_obj2 = MyClass(20)

MyClass.class_method(5)  # adds 5 to class_variable
print(MyClass.class_variable)  # output: 5

my_obj1.class_method(10)  # adds 10 to class_variable
print(MyClass.class_variable)  # output: 15

"""
@staticmethod, on the other hand, is used to define a method that is bound to 
the class and not the instance of the class, but it does not take any special 
first argument like cls. It is mainly used to group utility functions related
to the class, which do not require access to the class or instance state.

In this example, the static_method() function does not require access to the 
instance or class state, so it is defined as a @staticmethod. Note that we can 
call the method using the class name MyClass without instantiating the class.
"""

class MyClass:
    @staticmethod
    def static_method(x, y):
        return x + y
    
print(MyClass.static_method(2, 3))  # output: 5
