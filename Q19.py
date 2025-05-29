

        # Adding two list elements together


"""
Q: How can you add elements of two lists together in Python (element-wise
addition)? Write a function to perform this task and explain how it works)

A: In Python, You can add the elements of two lists together using a loop 
or a comprehension. or by using built-in tools like zip() to iterate over 
both lists at the same time. This is useful in mathematical or data-processing tasks."""



def add_lists(list1, list2):
    return [a + b for a, b in zip(list1, list2)]



# Test cases
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(f"The sum of {list1} and {list2} is: {add_lists(list1, list2)}")