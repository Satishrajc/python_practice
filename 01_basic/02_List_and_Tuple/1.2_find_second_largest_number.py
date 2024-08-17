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

find_second_largest([1, 2, 3, 4, 5])
find_second_largest([1, 1, 1])