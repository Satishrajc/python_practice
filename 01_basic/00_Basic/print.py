
print("Hello")

name = input("Enter a your name: ")
age = input("Enter a your age: ")


print(f"type: {type(name)} : {name}")
print(f"type: {type(age)} : {age}")

# By defaulr end="\n"Satish
print("Hi End with something", end="|")
print("next string")

# ---------------------------------------------------------------------
name, age = "Satish", 32
print(f"Name : {name: >20} and age {age}")
print(f"Name : {name: <20} and age {age}")
print(f"Name : {name: ^20} and age {age}")

# ---------------------------------------------------------------------

# Taking comma separated multiple inputs
data = input("Entrer comma separated inytergers: ").strip().split(" ")
print("Comma spearted inputs: ", data)