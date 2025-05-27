

        # Q16: Finding the Minimum Number in a list

"""
Q: How can you find the ninimum number in a list using Python?
Write a function to do this and exaplain how it works.

A: To find the smallest number in a list, we can write a custom function 
using a loop. This approach avoids built-in funciton like min() and shows problem-solving logic."""


def find_minimum(lst):
    min_num = lst[0] # Assume the first element is the minimum initially
    for num in lst:
        if num < min_num:
            min_num = num # Update min_num if a smaller number is foround

        
    return min_num


# Test case
lst = [-2, 14, 25, -33, 222]
print(f'The minimum number in the list {lst} is {find_minimum(lst)}')






# You can also use the built-in min function for a more concise solution

lst = [3, 4, 6, 7, 8, 12, 77, 90]
min_value = min(lst)
print(f'Min value in the list {lst} is {min_value}')