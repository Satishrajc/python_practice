class MyClass:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return "String representation for end user"

    def __repr__(self):
        return "String representation for debugging"

    @classmethod
    def from_class_method(cls, name, age):
        print("Class method")
        return cls(name, age)

    @staticmethod
    def from_staticmethod():
        print("staticmethod")

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    @fullname.setter
    def fullname(self, name):
        self.first_name, self.last_name = name.split(' ')

    # self.last_name = last_name

    @fullname.deleter
    def fullname(self):
        print("In deleter")

        self.first_name = None
        self.last_name = None


# obj1 = MyClass("Satish", 30)
#
# MyClass.from_class_method("Dada", 34)
#
# obj1.from_staticmethod()

# ------------------------------------------
obj2 = MyClass("Mama", 50)
print(obj2)
# If we dont have __str__ then Python automatically calls __repr__
# reverse is not possible

# print(repr(obj2))
# print(str(obj2))
# -------------------------------------

# fullname can be called as a variable
print(obj2.fullname)

obj2.fullname = "Kaka 55"
print(obj2.fullname)

del obj2.fullname
