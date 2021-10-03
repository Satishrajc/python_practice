class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return "({0},{1})".format(self.name, self.salary)

    def __add__(self, other):
        return self.salary + other.salary

    def __sub__(self, other):
        return self.salary - other.salary


object1 = Employee('Satish', 100)
object2 = Employee('Niteen', 200)

# Use of operator overriding to add two objects
print("Addition: ", object1 + object2)
print("Subtraction: ", object1 - object2)
