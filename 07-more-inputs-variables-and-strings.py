#  MAIN CODE

#  Variables are declared and initialized.
name_first_user = ""
name_second_user = ""

age_first_user = 0
age_second_user = 0


#  The name and age of the first user are asked.
print(">>> FIRST USER <<<")
name_first_user = input("Hi, what's your name?: ")
print(f"Hello {name_first_user}")
age_first_user = int(input("And how old are you?: "))
print("Thank you very much for the information!")
print("\n")

#  The name and age of the second user are asked too.
print(">>> SECOND USER <<<")
name_second_user = input("Hi to you too,what's your name?: ")
print(f"Hello {name_second_user}")
age_second_user = int(input("And how old are you?: "))
print("Thank you very much for the information!")
print("\n")

#  The ages are compared and, depending on the result, one message or another is displayed.
if age_first_user > age_second_user:
    print(name_first_user + ", you are older than " + name_second_user)
elif age_first_user < age_second_user:
    print(name_first_user + ", you are younger than " + name_second_user)
else:
    print(name_first_user + ", you are the same age as " + name_second_user)
print("\n")
