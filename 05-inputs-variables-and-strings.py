#  MAIN CODE

#  A variable is declared.
greeting_string = ""

#  The username is requested in the console.
nombre = input("What's your name?: ")
print("\n")

#  A string of characters is stored in the variable.
greeting_string = "Hi " + nombre + ", my best regards."

#  String is displayed in console.
print(greeting_string)
print("\n")

#  The length of the string is calculated and a message is displayed in the console.
print(
    "Did you know that the length of this greeting is "
    + str(len(greeting_string))
    + " characters?."
)
print("\n")
