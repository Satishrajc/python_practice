''''
The child classes can inherit methods and attributes from the parent class. We can redefine certain
methods and attributes specifically to fit the child class, which is known as Method Overriding.
Polymorphism allows us to access these overridden methods and attributes that have the same name as
the parent class.
'''


class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"{self.name} {self.age}")


class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method overriding
    def info(self):
        print(f"{self.name} {self.age}")


obj_parent = Parent("Parent", 60)
obj_child = Child("Child", 30)

obj_parent.info()
obj_child.info()
