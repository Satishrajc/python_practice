class MyException(Exception):
    def __init__(self, msg):
        super(MyException, self).__init__(msg)


print('Before Exception')

try:
    raise MyException('Custom message')

except MyException as e:
    print(e)
else:
    print('Exception does not happened')
finally:
    print('Finally we are at the end of script')

print('After Exception')
