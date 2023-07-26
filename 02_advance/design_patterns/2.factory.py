# The Factory pattern provides an interface to create objects of a superclass, allowing the 
# subclasses to alter the type of objects that will be created. It promotes loose coupling by 
# hiding the object creation logic from the client code.
# The key features of the Factory pattern are:

# A Factory class with a method that creates objects of different subclasses based on certain criteria.
# A common superclass or interface for the objects that the Factory creates.

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Invalid animal type")

# Usage
factory = AnimalFactory()
dog = factory.create_animal("dog")
cat = factory.create_animal("cat")

print(dog.speak())  # Output: "Woof!"
print(cat.speak())  # Output: "Meow!"
