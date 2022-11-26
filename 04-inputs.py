""" MAIN CODE """


"""
The user is asked in the console and the answer is stored in a variable.
The console response always returns a string.

"""
name = input("What's your name?: ")
print("\n")

""" Different ways to display user response in console. """
print(name)
print("\n")
print("Your name is " + name)
print("\n")
print("Your name is", name)
print("\n")
print(f"Your name is {name}")
print("\n")

"""
The user is asked for a number in the console and the answer is stored in a variable.
The console response always returns a string.

"""
number = input("Enter a number that will be multiplied by two: ")
print("\n")

""" If you want to operate with the number, you have to convert it to an integer. """
number = int(number) * 2

""" To show it again in console, you have to convert it to string """
print(str(number))
print("\n")

""" Another way """
number = int(input("Enter a number that will be multiplied by two: "))
print("\n")
number = number * 2
print(str(number))
print("\n")
