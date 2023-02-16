#  MAIN CODE

def sum(a, b):
    """
    This Python function takes two arguments (a and b) and returns the sum of
    the two as a result.

    Args:
        a (integer): First argument.
        b (integer): Second argument.

    Returns:
        integer: Returns the sum of the two arguments.
    """
    total = a + b
    return total

#  This line prints the result of the sum function with arguments 3 and 2.
print("\n")  # Line break.
print(sum(3, 2))
print("\n")  # Line break.

def full_name(name, last_name, inverse=False):
    """
    This function takes two arguments, 'name' and 'last_name', and combines them into a
    string with the first name first followed by the last name. If the optional argument
    'inverse' is set to True, then the names will be reversed with the last name first
    followed by the first name. The function will return the resulting string.

    Args:
        name (string): name
        last_name (string): last name
        inverse (bool, optional): inverse order, defaults to False.

    Returns:
        string: The function returns the first and last name depending on the arguments.
    """
    if inverse:
        return f"{last_name} {name}"
    else:
        return f"{name} {last_name}"

# Print the full name without the inverse parameter.
print(full_name("Michael", "Smith"))
print("\n")  # Line break.

# Print the full name with the inverse parameter.
print(full_name("Michael", "Smith", inverse=True))
print("\n")  # Line break.

# Print the full name using keyword arguments
print(full_name(last_name="Smith", name="Michael"))
print("\n")  # Line break.
