
# Import the method collections.counter to count the frequency of characters in the strings
from collections import Counter


    # Comparing Two Strings for ANAGRAMS


""""
Q: How can you check if two strings are anagrams in Python? 
Write a function to perform this check and explain how it works.

A: Two strings are called anagrams if they contain the same characters with the same
frequency, but in a different order."""

def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)


# Test cases
str1 = 'listen'
str2 = 'silent'
str3 = 'hello'
print(f"Are '{str1}' and '{str2}' anagrams? {are_anagrams(str1, str2)}")
print(f"Are '{str1}' and '{str3}' anagrams? {are_anagrams(str1, str3)}")



# Using collections.Counter to check for anagrams
def are_anagrams_counter(str1, str2):
    return Counter(str1) == Counter(str2)


# Test cases using Counter
print(f"Are '{str1}' and '{str2}' anagrams (using Counter)? {are_anagrams_counter(str1, str2)}")
print(f"Are '{str1}' and '{str3}' anagrams (using Counter)? {are_anagrams_counter(str1, str3)}")