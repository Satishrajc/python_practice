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


p1 = Point(2, 3)
p2 = Point(-1, 2)
print(p1 + p2)

print('------')
print("SUB")
p3 = Point(3, 5)
p4 = Point(4, 4)
print(p3 - p4)
