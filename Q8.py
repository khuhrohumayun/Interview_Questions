   # Swapping Variable Values Without an intermediay Variable


"""
Problem: You have two variables, a and b, and you want to swap their values
without using a intermediary variable. This operation is commonly referred
to as a "Value Swap"

Solution: In Python, you can swap the values of a and b without using an 
intermediary variable using tuple unpacking. Here's the solution:
"""

a = 55
b = 44

print(f"Before Swaping {a} and {b}..")

# swap values
a, b = b, a

print(f"After Swaping {a} and {b}")