

            # Counting white spaces in a given string

""""
Q: How can you count the number of white spaces in a given string using Python?
A: To count the number of white spaces in a string, we can iterate through the string and check each character to see if it is a whitespace character. Alternatively, we can use the built-in `count` method to directly count spaces.
"""


def count_whitespaces(s):
    count = 0
    for char in s:
        if char.isspace():
            count += 1

    return count



# Test case
test_string = "Hello, how are you?"
result = count_whitespaces(test_string)
print(f"Number of white spaces in the given string: {result}")






# Using the built-in count method for a more concise solution
def count_whitespaces_builtin(s):
    return s.count(' ') # Counts only spaces, not other whitespace characters like tabs or newlines


# Test case using built-in method
String = "P r o g r a m m ing  is  fun !"
result = count_whitespaces_builtin(String)
print(f"Number of white spaces in the given string using built-in method: {result}")
