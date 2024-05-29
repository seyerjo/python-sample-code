"""  EXAMPLES of working with character strings and the escape character ('\')

"""
print("\n")
print("--------\nEXAMPLES\n--------")
print("\n")

#  1. Four lines of text are displayed on the console with a single 'print' statement.
print("Line 1.\nLine 2.\nLine 3.\nLine 4.")
print("\n")

#  2. Four lines of text with four columns each with a single 'print' statement are displayed on the console.
print("A\tB\tC\tD\nE\tF\tG\tH\nI\tJ\tK\tL\nM\tN\tO\tP")
print("\n")

#  3. How it's displayed in console the escape character?
print("This is the slash character: /.\nThis is the backslash character: \\.")
print("\n")

#  4. The escape character is used to be able to display single or double quotes.
print("\"Y\" isn\'t a number.")
print("\n")

#  5. All the examples seen above are combined into one, with the addition of the use of the 'input' statement.
print ("\nYour name is:\n" + "\"" + input("What's your first name: ")+ " " + input("What's your last name: ") + "\"\n")