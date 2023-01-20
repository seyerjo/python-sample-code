#  GLOBAL VARIABLES

my_first_string = "123"
my_second_string = "456"
my_third_string = "Hip"
my_fourth_string = "hurra"
my_other_string = "World"


#  MAIN CODE

#  String is displayed in console.
print(my_first_string)
print("\n")

#  The string is displayed in console in triplicate.
print(my_first_string * 3)
print("\n")

#  Concatenated strings.
print(my_first_string + my_second_string)
print("\n")

#  String duplicate and concatenation.
print(((my_third_string + " ") * 2) + my_fourth_string)
print("\n")

#  String duplicate and concatenation using 'Format' function.
print(f'{((my_third_string + " ") * 2)}hurra')
print("\n")

#  String length.
print(len(my_other_string))
print("\n")

#  A string is an array of characters.
print(my_other_string[0])
print(my_other_string[1])
print(my_other_string[2])
print(my_other_string[3])
print(my_other_string[4])
print("\n")

#  The string is displayed from the third character.
print(my_other_string[2:])
print("\n")

#  The first three characters are displayed.
print(my_other_string[:3])
print("\n")

#  Display the string from the beginning minus the last character.
print(my_other_string[:-1])
print("\n")

#  The odd letters of the string are displayed.
print(my_other_string[::2])
print("\n")

#  Normal concatenation.
print("I am a citizen of the " + my_other_string)
print("\n")

#  Concatenation with the 'Format' function.
print(f"I am a citizen of the {my_other_string}")
print("\n")

#  Multiplicity with the 'Format' function.
print(f"I am a citizen of the {my_other_string}, " * 20)
print("\n")
