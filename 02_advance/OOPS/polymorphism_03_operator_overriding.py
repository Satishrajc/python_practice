class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __sub__(self, other):
        result = self.x - other.x
        return result


print("ADDITION")
object1 = Point(2, 3)
object2 = Point(-1, 2)

# Use of operator overriding to add two objects
print(object1 + object2)

print('------')
print("SUBTRACTION")
object3 = Point(3, 5)
object4 = Point(4, 4)
print(object3 - object4)
