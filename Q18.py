


        # Converting list to string


"""
Q: How can you convert a list of items into a single string in Python?
Write a function to perform this task and explain how it works.

A: In Python, you can convert a list into a string by using the join()
method. This is useful when you want to display or save the list as a single
string (especially for lists of characters or words)."""



# Function to convert a list to a string
def list_to_string(list):
    return ''.join(list)




# Test cases
# use input to get a list from the user
list = input('Enter some text separated by commas: ').split(',')
print(f"The list as a string is: {list_to_string(list)}")


list = ['Machine ', 'Learning ', 'is ', 'fun!']
print(f"The list {list} as a string is: '{list_to_string(list)}'")
