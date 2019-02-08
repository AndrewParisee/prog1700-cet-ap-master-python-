# Program 1 - Desk Calculator
# A carpenter needs a program that computes the price of any desk a customer orders based on the following:
# order number, desk length in inches and width in inches, type of wood (“mahogany”, “oak” or “pine”), and
# number of drawers. The price computed as follows:
# - The charge for all desks is a minimum $200.
# - If the surface (length * width) is over 750 square inches, add $50.
# - If the wood is "mahogany" add $150; for "oak" add $125. No charge is added for "pine".
# -  For every drawer in the desk, there is an additional $30 charge.
# First, create a flowchart that clearly shows all of the paths of execution that will exist within your designed
# solution to this problem. Then, write a console application that will input the order number, desk length, desk
# width, type of wood and number of drawers and then output the corresponding price.
print ("Program 1 - Desk Calculator")
print ("")
# Define Variables
base_charge = 200
mahogany = ""
oak = ""
pine = ""
order_number = input("Enter Order Number: ")
length_of_desk = int(input("Enter the Length of the Desk (inches): "))
width_of_desk = int(input("Enter the Width of the Desk (inches): "))
type_of_wood = str(input("Enter the Type of Wood (Mahogany, Oak, Pine): "))
number_of_drawers = int(input("Enter the Number of Drawers: "))

# Perform Calculations
surface = length_of_desk * width_of_desk
if surface > 750:
    base_charge = base_charge + 50

if type_of_wood == "mahogany":
    base_charge = base_charge + 150

elif type_of_wood == "oak":
    base_charge = base_charge + 125

else:
    base_charge = base_charge + 0

cost_of_drawers = number_of_drawers * 30
total_cost = cost_of_drawers + base_charge

# Print Results
print ("")
print ("The Total Cost for Order " + order_number + " is: {:.2f}".format(total_cost))