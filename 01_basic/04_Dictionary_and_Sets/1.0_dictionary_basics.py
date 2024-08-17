D = {'name': 'Satish', 'age': 30, 'gender': "M"}

counter = 1
for i in (dir(D)):  # dir(D) gives a list of valid attributes for the dictionary 'D'
    if not i.ljust(8).startswith('__'):  # Skip special methods with '__'
        print(f"{counter}. {i}()")  # Print the non-special method
        counter += 1

print("\nD         :  ", D)  # The original dictionary
print("copy      :  ", D.copy())  # Creates a shallow copy of the dictionary

# Create a new dictionary with keys from the specified iterable and all values set to None
print("fromkeys  :  ", D.fromkeys((1, 2, 'Satish', 4, 5), None))

# Attempt to get the value for the key 'MAMA', which does not exist; return 'Not found' instead
print("get       :  ", D.get('MAMA', 'Not found'))

# Returns a view of the dictionary's key-value pairs
print("items     :  ", D.items())

# Returns a view of the dictionary's keys
print("keys      :  ", D.keys())

# Add key 'gender' with a value 'male' only if 'gender' doesn't already exist (which it does)
D.setdefault('gender', 'male')
print("setdefault:  ", D)  # No changes since 'gender' already exists

# Update the dictionary with the new key-value pairs
D.update({'Country': 'India', 'language': 'Kannada'})
print("update    :  ", D)

# Returns a view of the dictionary's values
print("values    :  ", D.values())

# Remove and return the last key-value pair from the dictionary (as a tuple)
print("popitem   :  ", D.popitem())

print("\nD -- ", D)  # Dictionary after popitem() was called

# Remove and return the value of the specified key ('age')
print(f"D.pop('age') : {D.pop('age')}")
print("D after popping the age       :  ", D)

# Clear all elements from the dictionary
print("clear     :  ", D.clear())

# Print the now empty dictionary
print("D after clear()              :  ", D)
