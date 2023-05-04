"""
Write a function to flatten a nested dictionary.
Write a function to get the n largest items in a dictionary.
Write a function to group a dictionary by its values.
Write a function to get the average value for each key in a dictionary of lists.
Write a function to count the number of occurrences of a key in a list of dictionaries.
Write a function to remove duplicate dictionaries from a list.
Write a function to get the key-value pairs that appear in both dictionaries.
Write a function to get the difference between two dictionaries, including added and removed keys.
Write a function to update a dictionary with the values of another dictionary, but only for keys that are present in both dictionaries.
Write a function to remove all items from a dictionary whose keys are not present in a given list.


Merge two dictionaries.
Get the maximum and minimum value in a dictionary.
Find the key with the maximum value in a dictionary.
Sort a dictionary by its values.
Count the frequency of each element in a list and store the results in a dictionary.
Check if two dictionaries have the same key-value pairs.
Get the most frequently occurring value in a dictionary.
Find the difference between two dictionaries.
Remove the keys with the smallest values from a dictionary.
Convert a list of dictionaries to a dictionary of lists.
"""

# Merge two dictionaries.
def merge_dicts(dict1, dict2):
    print({**dict1, **dict2})
 
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = merge_dicts(dict1, dict2)

# Get the maximum and minimum value in a dictionary.
def get_max_min_values(d):
    values = list(d.values())
    return (max(values), min(values))


# Find the key with the maximum value in a dictionary.
def get_key_with_max_value(d):
    max_value = max(d.values())
    for key, value in d.items():
        if value == max_value:
            return key

# Sort a dictionary by its values.

def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

# Count the frequency of each element in a list and store the results in a dictionary.
def count_elements_in_list(lst):
    freq_dict = {}
    for element in lst:
        if element in freq_dict:
            freq_dict[element] += 1
        else:
            freq_dict[element] = 1
    return freq_dict


# Check if two dictionaries have the same key-value pairs.
def count_elements_in_list(lst):
    freq_dict = {}
    for element in lst:
        if element in freq_dict:
            freq_dict[element] += 1
        else:
            freq_dict[element] = 1
    return freq_dict

# Get the most frequently occurring value in a dictionary.
def get_most_frequent_value(d):
    values = list(d.values())
    most_frequent_value = max(set(values), key=values.count)
    return most_frequent_value

# Find the difference between two dictionaries.
def find_difference(dict1, dict2):
    diff = {}
    for key, value in dict1.items():
        if key not in dict2 or dict2[key] != value:
            diff[key] = value
    return diff

 
# Remove the keys with the smallest values from a dictionary.
def remove_smallest_values(d):
    min_value = min(d.values())
    keys_to_remove = [key for key in d if d[key] == min_value]
    for key in keys_to_remove:
        del d[key]
    return d

# Convert a list of dictionaries to a dictionary of lists.
def list_of_dicts_to_dict_of_lists(list_of_dicts):
    dict_of_lists = {}
    for dictionary in list_of_dicts:
        for key, value in dictionary.items():
            if key not in dict_of_lists:
                dict_of_lists[key] = [value]
            else:
                dict_of_lists[key].append(value)
    return dict_of_lists