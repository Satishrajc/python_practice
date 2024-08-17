"""
list of the 10 interview problems:

Write a Python function to reverse a list.
Write a Python function to check if a list is sorted (either ascending or descending).
Write a Python function to find the maximum and minimum values in a list.
Write a Python function to remove duplicates from a list.
Write a Python function to find the second largest number in a list.
Write a Python function to find the common elements between two lists.
Write a Python function to merge two sorted lists into a single sorted list.
Write a Python function to rotate a list by k elements to the right.
Write a Python function to find the kth smallest element in a list.
Write a Python function to find the maximum sum subarray of a list.
"""

# Write a Python function to reverse a list.

def reverse_list(L):
    print("Method 1" , L[::-1])

    L.reverse()
    print("Method 2" ,L)

# reverse_list([1, 2, 3, 4, 5])

# Write a Python function to check if a list is sorted (either ascending or descending).

def is_sorted(L):
    ascending_sorted = sorted(L)
    descending_sorted = ascending_sorted[::-1]
    print(ascending_sorted)
    print(descending_sorted)

    if ascending_sorted == L or descending_sorted == L:
        print("Sorted")
    else:
        print("Not Sorted")
    # print(L == sorted(L) or L == sorted(L, reverse=True))

# is_sorted([1, 2, 3, 4, 5])
# is_sorted([5, 4, 3, 2, 1])
# is_sorted([1, 3, 2, 4, 5])


# Write a Python function to find the maximum and minimum values in a list.
def find_min_max(lst):
    print(f"Max: {max(lst)}")
    print(f"Min: {min(lst)}")

# find_min_max([3, 2, 1, 5, 4])

# Write a Python function to remove duplicates from a list.
def remove_duplicates(lst):
    print(list(set(lst)))

# remove_duplicates([1,2,34,1,2,3])


# Write a Python function to find the second largest number in a list.
def find_second_largest(lst):
    if len(lst) < 2:
        return None
    largest = second_largest = float('-inf')
    for x in lst:
        if x > largest:
            second_largest = largest
            largest = x
        elif x > second_largest and x != largest:
            second_largest = x
    print(second_largest if second_largest != float('-inf') else None)

# find_second_largest([1, 2, 3, 4, 5])
# find_second_largest([1, 1, 1])


# Write a Python function to find the common elements between two lists.
def find_common_elements(lst1, lst2):
    # print([i for i in lst1 if i in lst2])
    print(list(set(lst1) & set(lst2)))
# find_common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7])

# Write a Python function to merge two sorted lists into a single sorted list.
def merge_sorted_lists(lst1, lst2):
    lst1.extend(lst2)
    print(sorted(lst1))

# merge_sorted_lists([1, 3, 5], [2, 4, 6])

# Write a Python function to rotate a list by k elements to the right.
def rotate_list(lst, k):
    # Method 1
    lst1 , lst2= lst[k+1:], lst[:k+1]
    lst1.extend(lst2)
    print(lst1)

    # Method 2
    k %= len(lst)
    print(lst[-k:] + lst[:-k])

# rotate_list([1, 2, 3, 4, 5], 2)

# Write a Python function to find the kth smallest element in a list.
def find_kth_smallest(lst, k):
    print(sorted(lst)[k-1])

find_kth_smallest([1, 2, 3, 4, 5], 3) 

# Write a Python function to find the maximum sum subarray of a list.