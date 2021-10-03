'''

Here we changing all the class variable and methods in class 'MyClass" to upper case
'''


class MetaClass(type):
    def __new__(mcs, class_name, inherited_classes, attributes):
        print("in __new__")
        # print(f'class_name: {class_name:>15}')
        # print(f'inherited_classes:', inherited_classes)
        # print(f'attributes: ', attributes)

        upper_case_var_method = {}
        for k, v in attributes.items():
            if k.startswith('__'):
                upper_case_var_method[k] = v
            else:
                upper_case_var_method[k.upper()] = v

        return type(class_name, inherited_classes, upper_case_var_method)


class Dummy:
    pass


class MyClass(Dummy, metaclass=MetaClass):
    x = 10
    y = 20

    def __init__(self, name):
        self.name = name

    def get_name(self):
        print(self.name)


'''
Run the code without creating object - output: in __new__
__new__ will be called even before creating the object

The parameters will be automatically passed to Meta class
'''

obj = MyClass('Satish')
# obj.get_name()  # Gives Error because we made everything in uppercase
obj.GET_NAME()
