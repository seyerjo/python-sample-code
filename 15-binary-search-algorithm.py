""" BINARY SEARCH Algorithm.

    The Binary Search Algorithm is an efficient search algorithm for finding an element in a
    sorted list. It works by measuring the middle of the list and determining if the sought
    element is greater or lesser than the element in the middle of the list. If it's greater,
    the lower half of the list is discarded and searched in the upper part; otherwise, the
    upper part of the list is discarded and searched in the lower part. This is repeated until
    the element is found or it is determined that it is not in the list.

    This code calculates the square root of a given integer number. It uses a binary search
    algorithm to find the answer, dividing the search range in half each time. The process
    starts with a lower limit of 0.0 and an upper limit of the given number, or 1.0, whichever
    is greater. The response is calculated as the midpoint of the limits. If the square of the
    response is less than the given number, the lower limit is changed to the response, otherwise
    the upper limit is changed to the response. The process is repeated until the difference
    between the square of the response and the given number is less than a certain amount
    (epsilon). After this, the response is printed as the square root of the given number.

"""

#  MAIN CODE

#  'objective' is assigned the value of the integer input by the user.
objective = int(input("Enter a integer number: "))
print("\n")  #  Line break.

# 'epsilon' is assigned a small value to define the precision of the result.
epsilon = 0.01

#  'low_limit' and 'high_limit' are initialized to 0.0 and the maximum of 1.0 and the objective respectively.
low_limit = 0.0
high_limit = max(1.0, objective)

#  'response' is initialized to the average of the low_limit and high_limit.
response = (high_limit + low_limit) / 2

#  While loop is used to find the square root of the objective until the difference between the
#  response squared and the objective is smaller than the epsilon.
while abs(response**2 - objective) >= epsilon:
    print(f"Low Limit = {low_limit}, High Limit = {high_limit}, Response = {response}")

    # The 'low_limit' and 'high_limit' are adjusted accordingly in the while loop.
    if response**2 < objective:
        low_limit = response
    else:
        high_limit = response

    response = (high_limit + low_limit) / 2

# Finally, the square root of the objective is printed out.
print("\n")  #  Line break.
print(f"The square root of {objective} is {response}")
