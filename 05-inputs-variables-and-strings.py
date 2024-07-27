#  FUNDAMENTALS

#  Python has dynamic typing
variable_x = 1  # Integer
variable_y = 3.75  # Float
variable_z= "characters string"  # String
print(variable_x, variable_y, variable_z)
print(type(variable_x), type(variable_y), type(variable_z))
print("\n")

variable_x ="new characters string" # Now is string
variable_y = 8 # Now is integer
variable_z = 4.25 # Now is float
print(variable_x, variable_y, variable_z)
print(type(variable_x), type(variable_y), type(variable_z))
print("\n")

#  MAIN CODE

#  A variable is declared and assigned at the same time.
greeting_string = ""

#  The name of the user is requested by console and stored in the variable.
nombre = input("What's your name?: ")
print("\n")

#  We assign to the variable a string consisting of a text and the variable ‘name’.
greeting_string = "Hi " + nombre + ", my best regards."

#  String variable is displayed in console.
print(greeting_string)
print("\n")

#  The length of the string is calculated and a message is displayed in the console.
print(
    "Did you know that the length of this greeting is "
    + str(len(greeting_string))
    + " characters?."
    # The system function ‘len’ returns an integer that has to be converted into
    # a string to be displayed on the console.
)
print("\n")
