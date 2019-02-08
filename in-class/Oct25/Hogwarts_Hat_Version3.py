# Create a Program that assigns you to a Hogwarts house.
# Get the Hogwarts Sorting Hat key functionality into a function
# that takes in the students name as a parameter and returns the house
# that they have been assigned to.
# Let's keep the cheat to put all the "Potters" and "Malfoys" in particular houses.
# Let's have a loop run the function 10 times so 10 students can be entered.
# We will calculate the totals on
# the number of students in each house.

print ("Hogwarts Sorting Hat:")
print ("The Hat Will Now Place You into a House.")
print ("")
# Define Variables
import random
random_number = random.randint(1,4)

def last_name(name):
    last_name = ""
    if name == "Potter":
        print("We know how this is going to go..")
        print("Gryffindor!")
    elif name == "Malfoy":
        print("We know how this is going to go..")
        print("Slytherin!")
    else:
        if random_number == 1:
            print("Gryffindor!")
        elif random_number == 2:
            print("Hufflepuff!")
        elif random_number == 3:
            print("Ravenclaw!")
        elif random_number == 4:
            print("Slytherin!")
    return name

entered_last_name = input("Please enter your last name (q to quit): ")

for students in range(10):
    if (last_name(entered_last_name)):
        print ("")
    else:
        print ("")
    print("")
    entered_last_name = input("Please enter your last name (q to quit): ")

print ("End of Program!")