class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"{self.name} {self.age}")


obj1 = MyClass("Satish", 30)

print(MyClass)
print(MyClass("Maya", 50))
print(obj1)
print(obj1.name)

obj1.gneder = "Male"
print(obj1.gneder)

# --------------------------
print("----------")
MyClass.info(obj1)
obj1.info()
obj1.name = "Dada"
print(obj1.name)
