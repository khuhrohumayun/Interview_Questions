


            # Removing all whitespaces in a string


""""
Q: How do you remove all whitespaces in a string using Python?
A: We can use the `replace()` method to remove all whitespace characters from a string.
"""

def remove_whitespaces(s):
    return s.replace(" ", "").replace("\t", "").replace("\n", "")



# Test case for removing whitespaces
test_string_whitespace = "Hello, how are you? \n\t 123!"
result_whitespace = remove_whitespaces(test_string_whitespace)
print(f"String after removing whitespaces: '{result_whitespace}'")






def remove_string(s):
    return s.replace(' ', "")



# Test case for removing spaces
test_string_remove = "Hello, how are you? 123!"
result_remove = remove_string(test_string_remove)
print(f"String after removing spaces: '{result_remove}'")

