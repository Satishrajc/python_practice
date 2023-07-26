class A:
    def greet(self):
        return "Hello from A"

class B(A):
    def greet(self):
        return "Hello from B"

class C(A):
    def greet(self):
        return "Hello from C"

class D(B, C):
    pass

print(D.__mro__)


# Note: To avoid the diamond problem, you can use a different approach for your 
# class hierarchy, such as using interfaces or abstract classes, or by reorganizing 
# the inheritance structure to avoid multiple inheritance in situations where it is not necessary."