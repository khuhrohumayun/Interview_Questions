

        # Counting Consonants in a Given Word


"""
Question: How would you count the number of consonants in a given word
using Python? Can you write a sample code to demonstrate this?

Answer: To count the number of consonants in a given word, the approach is similar to counting 
vowels. but a few differences in filtering.."""


def count_consonants(word):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in word:
        if char not in vowels and char.isalpha():
            count += 1

    return count

    
# Test case
word = "Hello World"
print(f"The number of consonants in '{word}' is {count_consonants(word)}")
