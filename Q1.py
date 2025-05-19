
# Q:1 Why would you use the pass statement

"""Problem: In Python, there are situations where you need a way to create a
placeholder or acknowledge an operation without specifying its details. This is
especially common during code development and design when certain parts
of your code are not yet fully implemented. """

"""Solution: The "pass" statement in Python serves as a simple solution to
address these situations. It is used in the following scenarios:"""



# Code Skeleton: use 'pass' as a placeholder when defining functions, classes, or code blocks that are not yet implemented.
def my_function():
    pass # Placeholder for future implementation


# Conditions Statements: use 'pass' in conditional statements where no action is required.
if condition:
    pass # Placeholder for future implementation    
else:
    pass # Acknowledge the False case without doing anything



# Empty Classes: For class definitons without attributes or methods, use 'pass' as a placeholder.
class MyClass:
    pass # Awaiting the addition of attributes and methods





# Exception Handling: In try-except blocks, use 'pass' to acknowledge exceptions without taking action.

try:
    # Code that might raise an exception
    pass # Placeholder for future implementation
except SomeException:
    pass # Acknowledge the exception without taking action



# Loops: In loops, use 'pass' to acknowledge an iteration without performing any action.
for item in my_list:
    pass # A Placeholder for future processing