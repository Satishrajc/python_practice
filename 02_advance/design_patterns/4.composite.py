# The Composite pattern treats individual objects and compositions of objects (groups) uniformly, 
# allowing you to work with complex hierarchies of objects in a tree-like structure. It is used 
# to represent part-whole hierarchies, making it easy to work with individual objects and groups 
# of objects in a uniform way.

# The key features of the Composite pattern are:

# A common Component interface that represents both individual objects and groups.
# Leaf classes that represent individual objects.
# Composite classes that represent groups and can contain both individual objects and other 
# composite objects.

class Component:
    def operation(self):
        pass

class Leaf(Component):
    def operation(self):
        print("Leaf: Performing operation")

class Composite(Component):
    def __init__(self):
        self._children = []

    def add(self, component):
        self._children.append(component)

    def remove(self, component):
        self._children.remove(component)

    def operation(self):
        print("Composite: Performing operation")
        for child in self._children:
            child.operation()

# Usage
leaf1 = Leaf()
leaf2 = Leaf()

composite = Composite()
composite.add(leaf1)
composite.add(leaf2)

composite.operation()
