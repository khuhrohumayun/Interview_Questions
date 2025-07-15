


            # implementing variable length argments in python


'''Q: How do you implement variable length arguments in Python?
A: In Python, we can use the `*args` syntax to allow a function to accept a variable number of positional arguments. This allows us to pass any number of arguments to the function, which are then accessible as a tuple within the function.
'''


def variable_length_args(*args):
    for arg in args:
        print(args)


# Test case for variable length arguments
variable_length_args(1, 2, 3, 'a', 'b', 'c')
# variable_length_args(1, 2, 3, 'a', 'b', 'c') will print:
# (1, 2, 3, 'a', 'b', 'c')