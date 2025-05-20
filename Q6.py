       # Accessing Attributes of Functions

"""Problem: You want to access an attribute of a function in Python and print its
value. Specifically, you want to print the value of the what attribute of the 
function my_function.

Solution: In Python, functions are objects, but they don't have attributes like
classes or instances. Attempting to access attributres directly from a function 
object will result in an AttributeError. Howerver, you can achieve a similar 
behavior by using a dictionary to store data associated with the function.

Here's the solution:
"""

def my_function():
    print(my_function.data['What'])


my_function.data = {'What': "Right"}
my_function()