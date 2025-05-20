  # Finding Unique Value in a List 

"""Problem: You have a list lst containing several values, and you want to 
extract only the unique values from the list.

Solution: To find and extract the unique values from a list in Python, you can
convert the list into set and then vack into a list. This process eliminates any
duplicate value. Here's the solution:"""


lst = [1, 2, 3, 4, 4, 6, 7, 3, 4, 5, 2, 7]
unique_values = list(set(lst))


# set(lst) removes duplicates
# list(set(lst)) converts the set back to a list
print(unique_values)
# Output: [1, 2, 3, 4, 5, 7]

