
    # Printing Odd Numbers Between 1 and 100

"""Problem: You want to print the odd numbers between 1 to 100 
in python using list comprehension.


Solution: You can achieve this by using list comprehension to
generate a list of odd numbers and then print the list."""


odd_numbers = [x for x in range(101) if x % 2 != 0]
print(odd_numbers)

# Output: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31,
# 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59,
# 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87,
# 89, 91, 93, 95, 97, 99]