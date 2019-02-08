"""
- Ask the user to enter the names of everyone attending a party.
- Sort the list of the party guests in alphabetical order.
- Ask the user for a numeric index of the guest to the output.
- Output the guest at the selected positions in the list.
- Try to handle the user entering both a non-numeric value for the index and a number out of range of the list gracefully
"""
# Define Variables
guest_list = [""]
new_guest = ""

# Perform Actions
while new_guest.lower() != "q":
    new_guest = input("Enter the Name of the Guest Attending the Party (q to quit): ")
    if new_guest.lower() != "q":
        guest_list.append(new_guest)
while True:
    try:
        guest_number = int(input("Which guest number do you want to see? "))
        # if guest_number < 0:
        #   raise ValueError("Lower than zero")
        print ("Guest {} is {}".format(guest_number,guest_list[guest_number]))
        break
    except ValueError:
        print ("You must enter an integer")
    except IndexError:
        print ("You must enter a valid position in the list")

#guest_list.sort()

# Print Results
# This code happens when while loop is done
#print ("The guest list is: ")
#for guest in guest_list:
    #print ("\t{}".format(guest))



