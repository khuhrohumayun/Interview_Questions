

        # Counting the number of accurances of a character in a String


"""
Question: How would you count the number of times a specific character appears in a given
string using Python? Explain your apprach with an example.

Answer: To count the number of occurrences of a specific character in a string, we can use
either a manual loop approach or a built-in Python method. The goal is to identify and count 
how many times a particular character is present in the string."""


# Example
def count_character(String, char):
    count = 0
    for c in String:
        if c == char:
            count += 1

    return count


# Test case
String = "Hello, how many times does the letter 'o' appear in this sentence?"
char = 'o'
print(f"The character '{char}' appears {count_character(String, char)} times in the string.")






# You can also use the built-in count method for a more concise solution
def count_character_builtin(String, char):
    return String.count(char)

# Test case using built-in method
print(f"The character '{char}' appears {count_character_builtin(String, char)} times in the string using built-in method.")
