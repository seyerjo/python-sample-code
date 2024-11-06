# This is a single-line comment.

"""
This is a multi-line comment
also known as a docstring.
It is often used to document functions, classes, modules, etc.
"""

'''
This is another type of multi-line comment
using single quotes.
'''

# Inline comment after a line of code
x = 10  # This is an inline comment

# Docstring and inline comment inside a function
def my_function():
    """This function calculates the square of a number.""" 
    y = 5
    # Calculates the square
    z = y * y
    return z

# Comment before a function call
result = my_function()
print(result) # Inline comment after a function call

# Code commented ignored by the interpreter
# if True:
#    print("This code will not be executed")

# Comment explaining a complex part of the code
# The following code block handles the ZeroDivisionError exception
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
