        # Q:2 Subtracting 1 from Each Element in a list

"""Problem: Given a list 1st with elements [2, 33,222, 14, 25], you want to subtract 1
from each element in the list. 


Solution: You can achieve this by using a list comprehension to create a new
list with the modified elements. Here's the solution in Python:
python 
"""


print("Before Subtracting 1 from each element in the list")
lst = [2, 33, 222, 14, 25]
print(lst)


result = [x - 1 for x in lst]
print("After Subtracting 1 from each element in the list")
print(result)
# Output: [1, 32, 221, 13, 24]