""" EXHAUSTIVE LISTING algorithm, also called GUESS AND CHECK.

    The exhaustive enumeration algorithm is a method of finding the optimal
    solution to a given problem. It uses a brute-force search of all possible
    solutions to a problem to find the best solution. This means the algorithm
    reviews all possible options and tries to evaluate each one to find the
    best solution. The exhaustive enumeration algorithm is useful when the
    number of possible solutions is small. However, it is inefficient when the
    number of possible solutions is large, as it would have to review each
    solution to find the best one.

    This Python code is an example of the Exhaustive Listing algorithm, also
    called Guess and Check. The algorithm requests the user to enter an integer
    number, then it iterates by adding one to the response until it is obtained
    that the square of the response is equal to the number entered by the user.
    If so, then the square root of the number can be calculated and if not, then
    the number entered by the user does not have an exact square root. 

"""

#  MAIN CODE

#  Variables are declared.
objective = 0
response = 0

#  The square root of a number that we will request from the user will be calculated.
objective = int(input("Enter a integer number, please: "))

#  Line break.
print("\n")

#  If the stored in 'response' squared is less than the number entered by the user...
while response**2 < objective:
    print(response)  #  'Response' is printed.
    response += 1  #  It iterates by adding one to response.

#  Line break.
print("\n")

#  If after iterating 'response' raised to the square, it is obtained that it is equal to the number entered by the user...
if response**2 == objective:
    #  Square root can be calculated.
    print(f"The square root of {objective} is {response}")
else:
    #  If not, the number entered by the user does not have an exact square root.
    print(f"{objective} does not have an exact square root")
