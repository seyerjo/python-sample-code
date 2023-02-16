#  MAIN CODE

#  This code uses two nested loops to print a series of numbers.

#  Two variables are declared for two counters, one for each loop.
external_counter = 0
internal_counter = 0

#  The outer loop will run 5 times.
while external_counter < 5:
  #  The inner loop will run 6 times.
  while internal_counter < 6:
    #  Print the current values of the counters.
    print(external_counter, internal_counter)
    #  Increment the internal counter.
    internal_counter += 1

  #  Increment the external counter.
  external_counter += 1
  #  Reset the internal counter to 0.
  internal_counter = 0

#  Print a blank line.
print("\n")
