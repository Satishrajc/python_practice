"""

Method resolution order:
In Python, every class whether built-in or user-defined is derived from 
the object class and all the objects are instances of the class object. 
Hence, the object class is the base class for all the other classes.

In the case of multiple inheritance, a given attribute is first searched in the current class if
it’s not found then it’s searched in the parent classes. The parent classes are searched in a
depth-first, left-right fashion and each class is searched once.
If we see the above example then the order of search for the attributes will be Derived, Base1,
Base2, object. The order that is followed is known as a linearization of the class Derived and this
order is found out using a set of rules called Method Resolution Order (MRO).

To view the MRO of a class:

Use the mro() method, it returns a list
Eg. Class4.mro()
Use the _mro_ attribute, it returns a tuple
Eg. Class4.__mro__

Super() is generally used with the __init__ function when the instances are initialized.
The super function comes to a conclusion, on which method to call with the help of the
method resolution order (MRO).
"""

# Python Program to depict multiple inheritance
# when method is overridden in both classes


class Class1:
    def m(self):
        print("In Class1")


class Class2(Class1):
    # def m(self):
    #     print("In Class2")
    pass


class Class3(Class1):
    # def m(self):
    #     print("In Class3")
    pass


class Class4(Class2, Class3):
    # def m(self):
    #     print("In Class4")
    pass


obj = Class4()
obj.m()

print(Class4.__mro__)
