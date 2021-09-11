class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"{self.name} {self.age}")

    def __str__(self):
        return "Information about class"

    def __repr__(self):
        return 'Information for developers'

    def __add__(self, other):
        # Same way we can do __sub__, __mul__, __div__
        return self.age + other.age

    def __len__(self):
        return 10

    def __eq__(self, other):
        return self.age + other.age


obj1 = MyClass("Satish", 30)

print("MyClass: ", MyClass)
print(MyClass("Maya", 50))
print("Obj: ", obj1)
print(obj1.name)

obj1.gneder = "Male"
print(obj1.gneder)

print("-" * 20)
MyClass.info(obj1)
obj1.info()
obj1.name = "Dada"
print(obj1.name)

print("-" * 20)

obj1 = MyClass('Niteen', 34)
obj2 = MyClass('Satish', 30)

print("Overded inbuilt '+': ", obj1+obj2)


print("-" * 20)
print("Overded len() : ", len(obj1))
