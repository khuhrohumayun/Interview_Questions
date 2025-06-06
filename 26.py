


            # Building a Pyramid in Python

"""
Q: How do you build a pyramid in Python?
A: We can use nested loops to print spaces and asterisks in a pyramid shape. The outer loop controls the number of rows, while the inner loops handle spaces and asterisks.
"""


def build_pyramid(rows):
    for i in range(rows):
        # Print leadind spaces
        for j in range(rows - i -1):
            print(" ", end= "")
        # Print asterisks
        for k in range(2 * i + 1):
            print("*", end="")
        print()


# Test case for building a pyramid
rows = int(input("Enter the number of rows for the pyramid: "))
build_pyramid(rows)