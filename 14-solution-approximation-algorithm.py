""" SOLUTION APPROXIMATION algorithm

    The approximation algorithm is a method for finding an approximate solution to a
    problem. This is achieved by using a series of iterative steps that are applied
    until a satisfactory solution is obtained.
    
    The basic steps followed to find the approximation to the solution are: 

    1. Define the problem.
    2. Establish the parameters of the solution.
    3. Generate an initial solution.
    4. Evaluate the initial solution.
    5. Generate a new solution.
    6. Re-evaluate the new solution.
    7. Compare the initial solution with the new solution.
    8. Repeat steps 5 to 7 until the approximate solution is found.
    
    This code is an approximation algorithm that tries to find the square root of
    an integer number given by the user.

    First, the user chooses a number and a constant "epsilon" is declared with a
    value of 0.01. This constant will control the level of accuracy of the algorithm.
    Then, a variable "response" is initialized at 0.0 which will then be incremented
    with the step of the algorithm.

    A while loop is initiated to calculate the square root of the number. The loop
    compares the square root of the response variable with the target number. If the
    difference is less than the epsilon value, the algorithm assumes it has found the
    answer. If the difference is greater, the loop continues and the response variable
    is incremented with the defined step.

    Finally, the algorithm checks if the square root of the response is within the epsilon
    margin and, if so, prints the response on the screen. If not, it prints a message
    indicating that the square root has not been found.

"""

#  MAIN CODE

#  Variables are declared.

#  Set the precision level of the algorithm. The more precision, the more computation time.
#  You must choose between the speed in obtaining the result versus the precision.
epsilon = 0.01

#  Step of the algorithm. Epsilon squared is smaller than epsilon.
step = epsilon**2

#  Response variable.
response = 0.0

#  Get number from user.
objective = int(input("Enter a integer number, please: "))

#  Line break.
print("\n")

#  Loop until the square root of the response is within the epsilon margin.
while abs(response**2 - objective) >= epsilon and response <= objective:
    print(abs(response**2 - objective), response)
    response += step

#  Line break.
print("\n")

#  If the square root of the response is within the epsilon margin, print the response.
if abs(response**2 - objective) >= epsilon:
    print(f"The square root of {objective} could not be found.")
else:
    print(f"The square root of {objective} is {response}.")
