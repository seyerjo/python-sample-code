""" GLOBAL VARIABLES """
greeting_string = ""


""" MAIN CODE """
nombre = input("What's your name?: ")
print("\n")

greeting_string = "Hi " + nombre + ", my best regards."

print(greeting_string)
print("\n")

print(
    "Did you know that the length of this greeting is "
    + str(len(greeting_string))
    + " characters?."
)
print("\n")
