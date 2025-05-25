    
    # Counting Vowels in a Given Word

"""
Question: How would you count the number of vowels in a given word 
using Python? Can you write a sample code to demonstrate this?

Answer: To Count the number of vowels in a given word, you can iterate through each character in the
word and check whether it is a vowel. Python makes this easy using a for loop and membership check with the in keyword."""



# Example:
def count_Vowels(word):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in word:
        if char in vowels:
            count += 1

    return count


# Test case
word = "Interview"
print(f"The number of vowels in '{word}' is {count_Vowels(word)}")


# you can also solve it in one line using list comprehension

sum(1 for char in word if char.lower() in 'aeiou')

print(word)