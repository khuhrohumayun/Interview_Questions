


            # Randomizing the items of a list in Python


""""
Q: How do you randomize the items of a list in Python?
A: We can use the `random.shuffle()` method from the `random` module to randomize the items of a list in Python.
"""

import random 

def randomize_list(items):
    random.shuffle(items)
    return items



# Test case for randomizing a list
items = [1, 2, 3, 4, 5]
print("Original list:", items)
randomized_items = randomize_list(items)
print("Randomized list:", randomized_items)

