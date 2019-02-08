# Create a Program that assigns you to a Hogwarts house.
print ("Hogwarts Sorting Hat:")
print ("The Hat Will Now Place You into a House.")
print ("")
# Define Variables
import random
random_number = random.randint(1,4)
last_name = input("Please Enter Your Last Name: ").upper()

# Perform Calculations
if last_name == "Potter".upper():
    print ("We know how this is going to go..")
    print ("Gryffindor!")
elif last_name == "Malfoy".upper():
    print ("We know how this is going to go..")
    print ("Slytherin!")
else:
    if random_number == 1:
        print ("Gryffindor!")
    elif random_number == 2:
        print ("Hufflepuff!")
    elif random_number == 3:
        print ("Ravenclaw!")
    elif random_number == 4:
        print("Slytherin!")

# Output Results
print ("")
print ("Congratulations! {}.".format(last_name.title()))