"""
Program 1 - Five Numbers:
Design and write a program that accepts five number values from the user, then displays different configurations
of those numbers as output.
Your solution should demonstrate an understanding of how to apply list and looping concepts in a program that should:
- Prompt the user to enter five numbers, and store them in the program.
- Reverse the five numbers from the user-entered order and display the reversed order onscreen.
- Calculate and display the average of the five numbers.
- Display a list of all numbers that are larger than the calculated average.
"""
print ("Program 1 - Five Numbers:")
print ("-----------------------------------")
# Define Variables
x = 0
value = list()

# Perform Calculations
while len(value) < 5:
    x += 1
    test = input("Enter value #{}: ".format(x))
    i = int(test)
    value.append(i)
# (print (*value,sep='\n')) - This would print the list in its original form

# Calculate the average of the list
avg = sum(value)/x

# Find the numbers greater than the average
value2 = sorted(filter(lambda x: x > avg, value))

# Prints Results
print ("-----------------------------------")
# Display List in reverse order
print ("Numbers In Reverse Order: ")
for i in reversed(value):
    print(i)
print ("-----------------------------------")
# Display the average of the list
print ("The Average of the Numbers is: {}".format(avg))
print ("-----------------------------------")
print ("Numbers Greater Than the Average: ")
print(*value2,sep='\n')