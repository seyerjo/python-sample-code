#  MAIN CODE

#  The user is prompted for two integers and their values are stored in two variables.
num_1 = int(input("Enter a first integer: "))
print("\n")
num_2 = int(input("Enter a second integer: "))
print("\n")

#  The responses are evaluated with an 'if-else' statement.
if num_1 > num_2:
    print("The first number is greater than the second.")
    print("\n")
elif num_1 < num_2:
    print("The second number is greater than the first.")
    print("\n")
else:
    print("The two numbers are the same.")
    print("\n")
