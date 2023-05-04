

from typing import Any


class Employee:
    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary

    def get_emp_details(self) -> None:
        print(f"Employee name : {self.name} and his/her salary is {self.salary}")

    def __add__(self, other) -> int:
        return self.salary + other.salary
    
    def __str__(self) -> str:
        return "Just to demonstrate dunder method : __str__"
    
    def __repr__(self) -> str:
        return "Just to demonstrate dunder methods: __repr__"
    
    # del __del__(self):
    #     print("deleting object")

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("Called __call__")
    
    def __len__(self):
        return f"Length of name {self.name} is {len(self.name)}"


emp_ramesh = Employee("Ramesh", 5000)
emp_suresh = Employee("Suresh", 1000)

emp_ramesh.get_emp_details()

print(emp_ramesh + emp_suresh)

print(emp_ramesh)
print(Employee)
len(emp_ramesh)
print(emp_ramesh())