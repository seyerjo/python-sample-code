#  VARIABLES

#  Stores the number entered by the user.
value = 0

# FUNCTIONS

def factorial(n):
    """
    Calculate the factorial of 'n'.

    Args:
        - n (integer) > 0.

    The function returns factorial of 'n'.
    If 'n' is equal to 1, this value is returned directly as a result of the function.
    The function is recursive because it calls itself.

    """

    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def request_number():
    """
    Prompts the user to enter an integer greater than zero.

    Args:
        - None.

    The character entered by the user is converted to an integer.
    The entered value is assigned to the global variable 'value'.
    The function is recursive because it calls itself.

    """

    #  The user is prompted for the value.
    value = int(input("Enter an integer greater than zero, please: "))

    #  If the global variable 'value' is greater than zero, the factorial of the value
    #  entered by the user is calculated and displayed on the console after a line break.

    #  If the global variable 'value' is not greater or equal than zero, the user is
    #  prompted again on the console after a line break.
    if value > 0:
        print("\n")
        print("El factorial de " + str(value) + " es " + str(factorial(value)))
    else:
        print("\n")
        request_number()

#  MAIN CODE

#  Presentation of the routine in the console between a pair of line breaks.
print("\n")
print(">>> Calculate the factorial of a number <<<")
print("\n")

# The user is prompted for a number.
request_number()
