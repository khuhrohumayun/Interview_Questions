

        # Write a program that prompts the user for a sentence and displays the number of vowels in the sentence.


"""
Q: Write a program that prompts the user for a sentence and displays the number of vowels in the sentence.
A: We can use a simple loop to iterate through each character in the sentence and count the vowels.

"""

def count_vowels(sentence):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1

    return count


# Test case for counting vowels in a sentence
sentence = input("Enter a sentence: ")
vowel_count = count_vowels(sentence)
print(f"The number of vowels in the sentence is: {vowel_count}")

