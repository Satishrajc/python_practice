'''

Inheritance method resolution MOR start form left to right
in this case Child --> Parent 1 --> Parent 2
'''

class Parent1:
    def __init__(self, name, age, salary):
        self.name = name
        self._age = age
        self.__salary = salary

    # def info(self):
    #     print('In Parent 1')


class Parent2:
    def __init__(self, name, age, salary):
        self.name = name
        self._age = age
        self.__salary = salary

    def info(self):
        print('In Parent 2')


class Child(Parent1, Parent2):
    def __init__(self, name, age, salary, other):
        super().__init__(name, age, salary)
        self.other = other

    def info(self):
        print('In Child')


obj = Child("Satish", 30, 10000, 'other')
# Comment method 'info' in child class, then from Parent1
obj.info()
