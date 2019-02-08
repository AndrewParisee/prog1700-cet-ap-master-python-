# New Test Comment

# Define Variables

#Original_Bill = 85
#tax = 0.15 * (Original_Bill)
#tip = 0.20 * (Original_Bill)

Bill = int(input("Enter your original bill amount: $"))
tax = 0.15 * Bill
tip = 0.20 * Bill

# Peform Calculations
#total = (Original_Bill) + (tax) + (tip)

total = Bill + tax + tip
 
# Output the Results
#print ("Your original bill amount is: $" + str(Original_Bill))
#print ("Your tax is: " + str(tax))
#print ("Your tip is: " + str(tip))
#print ("Your total is: $" + str(total))

print ("Your bill amount is: $" + str(Bill))
print ("Your tax is: $" + str(tax))
print ("Your tip is: $" + str(tip))
print ("Your total is: $" + str(total))