      # Performing Bitwise XOR


"""
Problem: You want to perform a bitwise XOR operation in Python to 
manipulate binary data or check for differences betweeen two binary numbers.

Solution: In Python, you can use ^ operator to perform a bitwise XOR
operation. Here's how you can do it.
"""

# XOR two integers
result = 7 ^ 3 # result will be 4

# XOR two binary numbers as integers
binary_result = int('10101', 2) ^ int('11010', 2) # binary_result wil be 15

# XOR two binary numbers as strings
binary_str1 = '10101'
binary_str2 = '11010'

# XOR operation using a loop for binary strings of the same length
result_str = ''.join(['1' if a != b else '0' for a, b in
                       zip(binary_str1, binary_str2)])

print(result_str) # '01111'