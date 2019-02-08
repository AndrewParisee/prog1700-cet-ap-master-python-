# Program 2 - Eureka Water Company:
# Eureka Water Company charges the homeowner a single rate based on the total amount of water used by a customer
# in the billing period. The amount charged will be calculated based on which of the following ranges their total
# water usage falls under:
# Total Water Usage:                                                  Rate of Charge:
# Up to and including 1000 cubic feet.                                $15.00 flat rate.
# Over 1,000 cubic feet and up to and including 2,000 cubic feet.     $0.0175 per cubic foot.
# Over 2,000 cubic feet and up to and including 3,000 cubic feet.     $0.02 per cubic foot.
# Over 3,000 cubic feet.                                              $70,00 flat rate.
#
# First, create a flowchart that clearly shows all of the paths of execution that will exist within your designed
# solution to this problem. Then, write a console application to input the customer’s usage in cubic feet and output
# the corresponding rate charge.
print ("Program 2 - Eureka Water Company")
print ("")
# Define Variables
charge = 0
usage_of_water = int(input("Enter Usage of Water (Cubic Feet): "))

# Perform Calculations
if usage_of_water <= 1000:
    cost = charge + 15
elif usage_of_water <= 2000:
    cost = usage_of_water * 0.0175
elif usage_of_water <= 3000:
    cost = usage_of_water * 0.02
elif usage_of_water > 3000:
    cost = charge + 70

# Print Results
print ("")
print ("The Total Charge is ${:.2f}.".format(cost))