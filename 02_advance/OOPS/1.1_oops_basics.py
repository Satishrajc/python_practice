class MyClass:
    # Class variable affects all the objects
    class_variable = "I am class variable"

    def __init__(self, name, public_var, protected_var):
        self.name = name
        self.public_var = public_var
        self._protected_var = protected_var
        self.__private_var = "private_var"

    def public_method(self):
        print("In public_method")

    def _protected_method(self):
        print("In _protected_method")

    def __private_method(self):
        print("In __private_method")

    def get_class_variable(self):
        # Observe need to use 'self' to access class variable
        print(f"class variable : {self.class_variable}")


class MyChild(MyClass):
    def __init__(self, name, public_var, protected_var):
        super().__init__(name, public_var, protected_var)


obj1 = MyClass("Satish", "age: 50", "salary:10k")
obj1.public_method()
obj1._protected_method()
print(f"class_variable: {obj1.class_variable}")

obj2 = MyClass("Niteen", "age: 60", "salary:20k")

MyClass.class_variable = "Changed class variable"
print(f"class_variable: {obj1.class_variable}")

# We can access private variables and methods as well
print(obj1._MyClass__private_var)
print(obj1._MyClass__private_method())

# ---------------------------------------------------

child_obj = MyChild("Rakesh", "age: 73", "salary:20k")
child_obj._protected_method()
# child_obj.__private_method() # Gives attribute error
