

             # Q15: Finding the Maximum Number in a list


"""
Q: How can you find the maximum number in a list using Python?
Write a function to do this and explain how it works.

A: In python, you can find the maximum number in a list either
by using the built-in 'max()' function or by writing your own functin using a loop."""


def find_maximum(lst):
    max_num = lst[0] # Assume the first element is the maximum initially
    for num in lst:
        if num > max_num:
            max_num = num # Update max_num if a larger number is found

    return max_num


# Test case
lst = [2, 33, 222, 14, 25]
print(f"The maximum number in the list {lst} is {find_maximum(lst)}")



# You can also use the built-in max function for a more concise solution
max_value= max([3, 4, 6, 7, 8, 12, 77, 90])
print(f'Max value in the list is {max_value}')