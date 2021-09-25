class Employee:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def mail(self):
        if self.first_name:
            return f'{self.first_name}.{self.last_name}@company.com'
        else:
            return 'Mail id does not exit'

    @mail.setter
    def mail(self, full_name):
        self.first_name, self.last_name = full_name.split(' ')

    @mail.deleter
    def mail(self):
        print(f'details are cleaned up')
        self.first_name, self.last_name = None, None


emp1 = Employee('Satish', 'Chougule')

# Observe we are calling method without parentheses
print('Initial mail id : ', emp1.mail)

# What if you want to change the mail address for existing emp (should not call __init__)
emp1.mail = 'Niteen Chougule'

print('Changed mail id : ', emp1.mail)

# Delete the Employee mail
del emp1.mail

print(emp1.mail)
