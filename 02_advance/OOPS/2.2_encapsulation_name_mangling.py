'''
Private methods are those methods that should neither be accessed outside the class nor by any base class.
In Python, there is no existence of Private methods that cannot be accessed except inside a class. However,
to define a private method prefix the member name with double underscore “__”.

To access private variables or methods need to use class name
syntax: object_name._ClassName__MethodName
'''


class MyClass:
    def __init__(self, protected_var, private_var):
        self._protected_var = protected_var
        self.__private_var = private_var

    def __private_method(self):
        print('This is private method')


obj = MyClass('Protected values', 'Private values')

print(f'Protectd: {obj._protected_var}')
print(f'Protectd: {obj._MyClass__private_var}')
obj._MyClass__private_method()
