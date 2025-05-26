

            # Q14: Write a fibanacci series    

"""
Q: How would you generate a Fibonacci series in Python? Exaplain 
you approach with an example.

A: The Fibonacci series is a sequence of numbers where each number is the sum
of the two preceding ones, it starts with 0 and 1. and continues like:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ..."""


# Function to generate Fibonacci series
def fibonacci_series(n):
    a, b = 0, 1
    print("Fibonacci series of", n, "is:")
    for i in range(n):
        print(a, end=' ')
        a, b = b,a + b # update the values of a and b



# Call the function with the number of terms
fibonacci_series(10)
