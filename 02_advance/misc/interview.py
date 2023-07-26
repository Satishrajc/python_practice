# Question: Counting Vowels
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum([1 for c in s if c not in vowels])

# result = count_vowels("Hello World")
# print(result)  # Output: 3 (count of 'e', 'o', and 'o')



# Question: Merge Two Sorted Lists
def merge_sorted_lists(list1, list2):
    L = []
    for i in zip(list1, list2):
        L.extend(i)
    return L

list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
merged_list = merge_sorted_lists(list1, list2)
# print(merged_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# Question: Longest Substring Without Repeating Characters
def length_of_longest_substring(s):
    char_index_map = {}
    max_length = 0
    start_index = 0

    for i, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start_index:
            start_index = char_index_map[char] + 1

        char_index_map[char] = i
        max_length = max(max_length, i - start_index + 1)

    return max_length

# result = length_of_longest_substring("abcabcbb")
# print(result)  # Output: 3 (longest substring is "abc")


# Question 1:
# Write a Python function to calculate the factorial of a given non-negative integer.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# factorial(5)

# Question 2:
# Write a Python function to check if a string is a palindrome (reads the same backward as forward).

def is_palindrome(s):
    if s == s[::-1]:
        print("palindrome")
    else:
        print("Not a palindrome")

# is_palindrome("madam")
# is_palindrome("dance")


# Question 3:
# Create a Python class representing a Circle. The class should have a constructor that 
# takes the radius as an argument and methods to calculate the area and circumference of 
# the circle.

class Circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = 3.14159 * self.radius * self.radius
        print(area)

    def circumference(self):
        circ = 2 * 3.14159 * self.radius
        print(circ)
    
# obj = Circle(5)
# obj.area()
# obj.circumference()

# Question 4:
# Write a Python function to find the maximum and minimum elements from a list of numbers.

def find_max_min(numbers):
    # Your code here
    numbers.sort()
    max, min = numbers[-1], numbers[0]
    print(max, min)

# find_max_min([2,4,6,74,3,2,1])


# Question 5:
# Write a Python function that takes a list of integers as input and returns a new list 
# containing only the even numbers from the original list.

def get_even_numbers(numbers):
    # Your code here
    print([i for i in numbers if i % 2 == 0])
    
# get_even_numbers([1,3,5,6,78,10])


# Question 10:
# Write a Python function to check if a given number is a prime number.

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# print(is_prime(10))

# Question 14:
# Write a Python function to check if two strings are anagrams of each other 
# (i.e., they contain the same characters but in a different order).

def are_anagrams(s1, s2):
    # Your code here
    return sorted(s1) == sorted(s2)
    
# print(are_anagrams("satish", "atishs"))


# Question 24:
# Write a Python function that takes a string and returns the count of each character 
# (case-insensitive) in the string as a dictionary.

def count_characters(s):
    # Your code here
    d = {}
    for i in s:
        if i not in d:
            d[i] = 0
        else:
            d[i] += 1            
    print(d)
    
    

# count_characters("wwwddssaarrrwww")

# Write a Python function that takes a list of words as input and returns a new list 
# containing the words sorted in ascending order of their lengths. If two words have 
# the same length, sort them in lexicographic order.

def sort_words_by_length(words):
    sorted_words = sorted(words, key=lambda word: (len(word), word))
    print(sorted_words)

# sort_words_by_length(["hiqiq", "wwwwwwwww", "qw"])

data = [(3, 9), (1, 5), (2, 2), (4, 7), (1, 3)]
sorted_data = sorted(data, key=lambda x: x[1])
# print(sorted_data)  # Output: [(2, 2), (1, 3), (1, 5), (4, 7), (3, 9)]


# Question 28:
# Write a Python function that takes a list of integers and returns the longest consecutive 
# ubsequence (in ascending order) present in the input list. If multiple consecutive subsequences 
# have the same length, return the first one encountered.

def longest_consecutive_subsequence(numbers):
    numbers_set = set(numbers)
    longest_subsequence = []
    current_subsequence = []

    for num in numbers:
        if num - 1 not in numbers_set:
            current_subsequence = [num]
            current_num = num + 1

            while current_num in numbers_set:
                current_subsequence.append(current_num)
                current_num += 1

            if len(current_subsequence) > len(longest_subsequence):
                longest_subsequence = current_subsequence

    return longest_subsequence


# Question 29:
# Write a Python class representing a LinkedList.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def remove_node(self, value):
        if not self.head:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next:
            if current_node.next.data == value:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def display_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

