class Parent:
    class_var = 'class_var'
    def __init__(self, public_var, protected_var, private_var):
        # Public variable
        self.public_var = public_var

        # Protected variable
        self._protected_var = protected_var

        # Private variable
        self.__private_var = private_var

    # Public method
    def public_method(self):
        return f'{self.public_var} - {self._protected_var} - {self.__private_var} - {self.class_var}'

    # Protected method
    def _protected_method(self):
        return f'{self.public_var} - {self._protected_var} - {self.__private_var}'

    # Public method
    def __private_method(self):
        return f'{self.public_var} - {self._protected_var} - {self.__private_var}'


class Child(Parent):
    def __init__(self, public_var, protected_var, private_var):
        super(Child, self).__init__(public_var, protected_var, private_var)

    # Public method
    def public_method(self):
        return f'{self.public_var} - {self._protected_var} {self.class_var}'
        # return f'{self.public_var}'


obj1 = Child('Satish', 'Chougule', '31')
print('public_var: ', obj1.public_var)
print('_protected_var: ', obj1._protected_var)

# Error:AttributeError: 'Parent' object has no attribute '__private_var'
# print('__private_var: ',obj1.__private_var)

print('----------')
print('public_method: ', obj1.public_method())

# Protected variable and method can be accessed in child class
print('_protected_method: ', obj1._protected_method())

# Error:AttributeError: 'Parent' object has no attribute '__private_var'
# print('__private_method: ',obj1.__private_method)


'''
Note: 
 - Only Protected variable/method can be accessed in child  lcass 
 - private variable/method can't be accessed in child class
 - Parent class variable can be accessed in child class
'''