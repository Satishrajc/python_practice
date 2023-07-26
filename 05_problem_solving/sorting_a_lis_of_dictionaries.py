# Write a Python program that sorts a list of dictionaries based on a specific key. 
# The program should take a list of dictionaries and a key as input and return the 
# sorted list of dictionaries based on the specified key.

def sort_list_of_dictionaries(data, key):
    sorted_data = sorted(data, key=lambda x: x[key])
    return sorted_data

# Test the sort_list_of_dictionaries function
data = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 22},
    {'name': 'Dave', 'age': 27}
]

sorted_data = sort_list_of_dictionaries(data, 'age')
print(sorted_data)
# Output: [{'name': 'Charlie', 'age': 22}, {'name': 'Alice', 'age': 25},
#          {'name': 'Dave', 'age': 27}, {'name': 'Bob', 'age': 30}]
