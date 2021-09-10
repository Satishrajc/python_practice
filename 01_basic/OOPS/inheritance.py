

class MyClass:
	def __init__(self, name, age, salary):
		self.name = name
		self._age = age
		self.__salary = salary

class SubClass(MyClass):
	def __init__(self, name, age, salary, other):
		super().__init__(name, age, salary)
		self.other = other

obj = MyClass("Satish", 30, 10000)
print(obj.name)
print(obj._age)
print(obj._MyClass__salary)


# --------------------

# objNew = SubClass("Data", 35, 20000, "Anna")
#
# objNew.name = "Kaka"
# print(objNew.name)
#
# objNew._age = 55
# print(objNew._age)

# objNew.__salary = 500000
# print(objNew._SubClass__salary)