# A fruit company sells oranges for 32 cents a pound plus $7.50 per order for shipping.
# If an order is over 100 pounds, shipping cost is reduced by $1.50.
# Pseudocode:
# 1. Enter pounds per orange variable (0.32).
# 2. Enter shipping cost variable (7.50).
# 3. Prompt user to enter the weight of their oranges.
# 4. If the weight of the oranges is above 100 pounds, decrease the shipping cost by 1.50.
# 5. Calculate the cost of the oranges by multiplying the weight by pounds per orange.
# 6. Add the shipping cost to the get the total cost.
# 7. Display the total cost of the oranges.
# 8. End program.

# Define Variables
pound_per_orange = 0.32
shipping = 7.50
weight = int(input("Enter the Weight of Your Oranges: "))

# Perform Calculations
if weight >= 100:   # between the if and the colon (:) - Boolean Expression
    # happens if the if expression is true
    shipping = shipping - 1.50

cost = weight * pound_per_orange + shipping

# Print Results
print ("")
print ("The Cost of Oranges That Weigh " + str(weight) + " Pounds is {:.2f}.".format(cost))