
import re

        # Counting Digits, Letters, and Spaces in a String

"""
Q: How can you count the number of digits, Letters, and Spaces in a given string using Python?
A: To count the number of digits, Letters, and Spaces in a string, we can iterate through the string and check each character to see if it is a digit, a letter, or a whitespace character. We can use the `isdigit()`, `isalpha()`, and `isspace()` methods for this purpose.
"""

# Using function to count digits, letters, and spaces in a string
def count_digits_Letters_Spaces(s):
    digits = 0
    Letters = 0
    Spaces = 0
    for char in s:
        if char.isdigit():
            digits += 1
        elif char.isalpha():
            Letters += 1
        elif char.isspace():
            Spaces += 1
    
    return digits, Letters, Spaces



# Test case
test_string = "Hello, how are you? 123"
result = count_digits_Letters_Spaces(test_string)
print(f"Number of digits: {result[0]}, Letters: {result[1]}, Spaces: {result[2]}")




# Using built-in methods for a more concise solution

name = 'Python is 1'

digitCount = re.sub("[^0-9]", "", name) 
lettercount = re.sub("[^a-zA-Z]", "", name)
spaceCount = re.sub("[^ ]", "", name)

print(f"Number of digits: {len(digitCount)}, Letters: {len(lettercount)}, Spaces: {len(spaceCount)}")
# Using regex to count digits, letters, and spaces in a string