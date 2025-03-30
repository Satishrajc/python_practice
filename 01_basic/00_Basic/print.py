
print("Hello")

name = input("Enter a your name: ")

print(f"type: {type(name)} : {name}")

# By defaulr end="\n"
print("Hi End with something", end="|")
print("next string")

# ---------------------------------------------------------------------
# Basic Variable Insertion
age = 30
print(f"My name is {name} and I am {age} years old.\n")

# Padding and Alignment
print(f"Name: {name:<10} (Left Aligned)")   # Left align (spaces added after the name)
print(f"Name: {name:>10} (Right Aligned)")  # Right align (spaces added before the name)
print(f"Name: {name:^10} (Center Aligned)\n")  # Center align

# Decimal Formatting
pi = 3.1415926535
print(f"Pi to 2 decimal places: {pi:.2f}")   # Output: 3.14
print(f"Pi to 4 decimal places: {pi:.4f}\n") # Output: 3.1416

# Leading Zeros
num = 42
print(f"Number with leading zeros: {num:05d}\n")  # Output: 00042

# Thousands Separator
large_number = 1234567890
print(f"Large number: {large_number:,}\n")  # Output: 1,234,567,890

# Hexadecimal, Octal, and Binary Representation
num = 255
print(f"Hexadecimal: {num:#x}")  # Output: 0xff
print(f"Octal: {num:#o}")        # Output: 0o377
print(f"Binary: {num:#b}\n")     # Output: 0b11111111

# Percentage Formatting
accuracy = 0.87234
print(f"Accuracy: {accuracy:.2%}\n")  # Output: 87.23%

# Scientific Notation
print(f"Scientific Notation: {large_number:.2e}")  # Output: 1.23e+09

# ---------------------------------------------------------------------

# Taking comma separated multiple inputs
data = input("Enter comma separated integers: ").strip().split(" ")
print("Comma separated inputs: ", data)