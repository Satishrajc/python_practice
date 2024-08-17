"""
10 coding questions on string data type:

Write a Python function to reverse a string.
Write a Python function to check if a string is a palindrome.
Write a Python function to remove all vowels from a string.
Write a Python function to find the first non-repeating character in a string.
Write a Python function to count the number of words in a string.
Write a Python function to find the most common character in a string.
Write a Python function to check if two strings are anagrams.
Write a Python function to find the longest common prefix of a list of strings.
Write a Python function to find the longest palindrome substring in a string.
Write a Python function to convert a string to title case.
"""

# Write a Python function to reverse a string.

def reverse_string(s):
    print(s[::-1])


# Write a Python function to check if a string is a palindrome.
def is_palindrome(s):
    print(s == s[::-1])
 

# Write a Python function to remove all vowels from a string.

def remove_vowels(s):
    vowels = "aeiouAEIOU"
    print("".join([c for c in s if c not in vowels]))

# Write a Python function to find the first non-repeating character in a string
def first_non_repeating_char(s):
    counts = {}
    # Counter to count number each char
    for c in s:
        counts[c] = counts.get(c, 0) + 1

    for c in s:
        if counts[c] == 1:
            print(c)
    return None

# Write a Python function to count the number of words in a string.
def count_words(s):
    print(*s)
    print(len(*s.split()))

# Write a Python function to find the most common character in a string.
from collections import Counter

def most_common_char(s):
    counts = Counter(s)
    print(counts)
    print(max(counts, key=counts.get))



# reverse_string("Satish")
# is_palindrome("madam")
# remove_vowels("Satish")
# first_non_repeating_char("ssDDmaak")
# count_words("Satishqqqq")
most_common_char("Saastishaa")

