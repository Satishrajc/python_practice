def decorator_function(f):
    def warper1(a, b):
        print('warper1')
        f(a, b)

    return warper1


class decorator_class():
    def __init__(self, func):
        self.func = func

    def __call__(self, a, b):
        self.func(a, b)


# @decorator_class

@decorator_function
def foo(a, b):
    print("Foo")


foo(10, 20)

# ---------------------------------------------------------
# def decorator_outside(message):
# 	def decorator_inside(f):
# 		def warper1(a,b):
# 			print(message)
# 			print('warper1')
# 			f(a,b)
# 		return warper1
# 	return decorator_inside
#
# @decorator_outside("Argument to decorator")
# def foo(a,b):
# 	print("Foo")
# foo(10,20)
