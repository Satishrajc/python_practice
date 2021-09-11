class A:
    a = 20
    def __init__(self, arg1):
        self.arg1 = arg1

    def get_info(self, extra_arg):
        print("Class A: " + self.arg1 + " " + extra_arg)


class B(A):
    def __init__(self, arg1):
        super(B, self).__init__(arg1)

    def get_info(self, arg1):
        super(B, self).get_info(arg1)
        print("Class B: " + self.arg1, self.a)




b_obj = B("Hello")
b_obj.get_info("Bye")

