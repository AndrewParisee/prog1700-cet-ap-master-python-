# Program 1 - PC Repair Shop
# McNair’s PC Repairs is a computer repair shop. Customers are billed at a rate of $65 per hour for labour.
# Costs for parts and supplies are subject to a 15% sales tax.
# You have been asked to develop a console application solution that will enable the company’s retail staff to track customer
# work orders. Begin by designing your solution to this problem in pseudocode, which will be submitted along with the program.
# The program user must be able to input the customer's name, the number of hours of labour, and the cost of any required
# parts or supplies. Once the input is provided, the program will display the customer's name and three calculated costs;
# labour cost, parts cost and total cost, as shown below.
# Pseudeocode:
# 1. Set Variables for customers name, hours of labour, and cost for parts.
# 2. Ask the user to input their name.
# 3. Ask the user to input the hours of labour.
# 4. Ask the user to enter the cost of any parts.
# 5. Calculate Labour cost by multiply hours by $65.
# 6. Calculate Parts cost by multiplying parts cost by tax, 15%.
# 7. Calculate Total cost by adding the labour costs to parts costs.
# 8. Display the customers name.
# 9. Display the labour cost.
# 10. Display the parts cost.
# 11. Print the total of all these costs.

print ("Program 1 - PC Repair Shop:")
print ("")
# Define Variables
name = input("Enter the customer's name: ")
hours = float(input("Enter the number of hours of labour: "))
parts_cost = float(input("Enter the cost of any parts and/or supplies: $"))

# Perform Calculations
labour = hours * 65
parts = parts_cost * 1.15
total = labour + parts

# Output Results
print ("")
print ("Work Order Summary For Customer, " + name + ":")
print ("Labour Cost: ${:.2f}.".format(labour))
print ("Parts Cost: ${:.2f}.".format(parts))
print ("Total Cost: ${:.2f}.".format(total))