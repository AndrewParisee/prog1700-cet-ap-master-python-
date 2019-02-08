# Define Variables
guest_list = ["Mike"]
new_guest = ""

# Perform Actions
while new_guest.lower() != "q":
    new_guest = input("Enter guest name (q to quit): ")
    if new_guest.lower() != "q":
        guest_list.append(new_guest)

guest_list.sort()

# Print Results
# This code happens when while loop is done
print ("The guest list is: ")
for guest in guest_list:
    print ("\t{}".format(guest))
