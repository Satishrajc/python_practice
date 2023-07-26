# Descriptors are objects that define how attribute access is handled within classes. 
# They allow controlling the behavior of attribute access (e.g., get, set, delete) by 
# defining __get__, __set__, and __delete__ methods.

class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self._temperature * 9/5) + 32

    def __get__(self, instance, owner):
        return self._temperature

    def __set__(self, instance, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not allowed.")
        self._temperature = value

class Temperature:
    celsius = Celsius()

temp = Temperature()
temp.celsius = 25
print(temp.celsius)  # Output: 25
print(temp.celsius.to_fahrenheit())  # Output: 77.0
