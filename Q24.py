


            # Counting Special Characters in a String

"""
Q: How do you count the number of special characters in a String using Python?
A: Specail characters are those that are not alphanumeric (letters and digits) or whitespace. We can use a regular expression to match these characters and count them.
"""


def count_special_characters(s):
    specail_count = 0

    for char in s:
        if not (char.isalpha() or char.isdigit() or char.isspace()):
            specail_count += 1

    return specail_count



# Test case for counting special characters

test_string_special = "Hello, how are you? @123!"
result_special = count_special_characters(test_string_special)
print(f"Number of special characters: {result_special}")