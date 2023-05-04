class Parent1:
    class_var = 10

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        print(f'Hi {self.name} and your age is {self.age}')

    def set_info(self, name):
        self.name = name


class Parent2:
    class_var = 10

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info1(self):
        print(f'Hi {self.name} and your age is {self.age}')

    def set_info(self, name):
        self.name = name


class Child(Parent1, Parent2):

    def __init__(self, name, age, gender):
        # Type 1
        # super(Child, self).__init__(name, age)

        # Type 1
        super(Parent2, self).__init__(name, age)
        # Parent2.__init__(self, name, age)

        self.gender = gender


    def get_info(self):
        print(self.class_var)
        print(f'Hi {self.name} and your age is {self.age} and you are {self.gender}')


obj = Child('Satish', 30, 'male')

obj.get_info()
