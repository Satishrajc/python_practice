class MyClass:
    class_variable = 'I am class variable'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"{self.name} {self.age}")

    def get_class_variable(self):
        # Observe need to use 'self' to access class variable
        print(f'class variable : {self.class_variable}')


obj1 = MyClass("Satish", 30)
obj1.info()
obj1.get_class_variable()
