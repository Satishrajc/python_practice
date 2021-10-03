class Employee:
    def __init__(self, name, salary, dept):
        self.name = name
        self.salary = salary
        self.dept = dept

    def salary_info(self, sal_amount):
        if sal_amount < self.salary:
            return self.name


obj1 = Employee('Satish', 100, 'ADAS')
obj2 = Employee('Niteen', 200, 'CARM')
obj3 = Employee('Rakesh', 300, 'ADAS')
obj4 = Employee('Deepa', 150, 'ADAS')
obj5 = Employee('Sina', 300, 'ADAS')

'''
Fetching salary of each class who is in ADAS
'''

L = [obj1, obj2, obj2, obj3, obj4, obj5]

department = 'ADAS'
L2 = []
for obj in L:
    if obj.dept == department:
        L2.append(obj.salary)

print(L2)