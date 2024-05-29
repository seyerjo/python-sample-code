#  MAIN CODE

#  Declared a list of numbers.
numbers = [1, 2, 3, 4, 5]

#  Print the list of numbers.
print("For this list of numbers:")
print(numbers)

#  Print a blank line
print("\n")

#  Declared a variable to hold the sum of the numbers.
sum = 0

#  Use a for loop to iterate over the list of numbers.
for number in numbers:
    # Add each number to the sum.
    sum += number

#  Print the sum of numbers.
print("The sum is: " + str(sum))

#  Print a blank line
print("\n")

#  Calculate the average of the numbers.
average = sum / len(numbers)

#  Print the result.
print("The average of the numbers is:", average)

#  Print a blank line
print("\n")
