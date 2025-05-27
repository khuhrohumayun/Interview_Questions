


        # Finding the middle Element in a list

""""
Q: How can you find the middle element of a list using Python?
Write a function and explain how it works. Also, explain what 
should happen if the list has an even number of elements.

A: To find the middle element of a list, we need to calculate the middle index.
If the list length is odd, return the element at the middle index.
If the list length is even, return the two middle elements or specify 
   how to handle it (e.g., return the average or just the lower/upper middle).)"""


def find_middle_element(lst):
    Length = len(lst)
    middle_index = Length // 2 # Calculate the middle index

    if Length % 2 == 1: # If the list has an odd number of elements
        return lst[middle_index]
    else: # If the list has an even number of elements
        return (lst[middle_index - 1], lst[middle_index])
    


# Test cases
list_odd = [1, 2, 3, 4, 5]
list_even = [1, 2, 3, 4, 5, 6]

print(f"The middle element of the odd list {list_odd} is {find_middle_element(list_odd)}")
print(f"The middle elements of the even list {list_even} are {find_middle_element(list_even)}")