# We want house lists that store all students added to each house. Print the lists at the end.
# We will no longer run 10 times, but will enter names until 'q' to quit.
print ("Hogwarts Sorting Hat:")
print ("The Hat Will Now Place You into a House.")
print ("")

# Define Variables
import random
random_number = random.randint(1,4)
wizard_list = [""]
last_name = ""

# Perform Actions

while last_name.lower() != "q":
    last_name = input("Enter your last name (q to quit): ")
    if last_name.lower() != "q":
        wizard_list.append(last_name)
        if last_name == "Potter".upper():
            print("We know how this is going to go..")
            print("Gryffindor!")
        elif last_name == "Malfoy".upper():
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

wizard_list.sort()

# Print Results
# This code happens when while loop is done

