
# The super().__init__(message) call is used to ensure that the base 
# Exception class is properly initialized with the provided message.

class MyException(Exception):
    def __init__(self, msg):
        super(MyException, self).__init__(msg)


print('Before Exception')

try:
    raise MyException('Custom message')

except MyException as e:
    print("User defined exception occurred: ", e)
else:
    print('Exception does not happened')
finally:
    print('Finally we are at the end of script')

print('After Exception')
