


        # Checking for Palindrome using extended Slicing Technique


""""
Q: How can you check if a String is a Palindrome in Python
Using the extended Slicing technique? Write a funcion and expalain how it works.

A: A Palindrome is a string that reads the same forward and backward."""


def is_palindrome(s):
    return s == s[::-1]



# Test cases
test_strings = ['radar', 'hello', 'level', 'world', 'madam']
for test in test_strings:
    result = is_palindrome(test)
    print(f"Is '{test}' a palindrome? {result}")