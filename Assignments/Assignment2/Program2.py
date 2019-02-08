# Program 2 - Car Loan Calculator
# Develop a car loan calculator program as a console application with the following specifications.
# Begin by designing your solution to this problem in pseudocode, which will be submitted along with the program.
# If A dollars are borrowed at r% interest compounded monthly to purchase a car with monthly payments for n years,
# then the monthly payment is given by the formula:
# If: i  =  r / 1200
# Then calculate the monthly payment as: monthly payment  = i / 1 – (1 + i)to the power of-12n * A
# Write a console application that calculates the monthly payment after the user gives the amount of the loan,
# interest rate, and number of years.
# Pseudocode:
# 1. Define amount, interest, and number of years variable.
# 2. Set rate variable and n and x variable to simplify calculations.
# 3. Ask the user to enter the amount of loan.
# 4. Ask the user to enter the interest rate.
# 5. Divide the interest rate by 1200.
# 6. Calculate the monthly payment by dividing rate by 1 subtract 1 plus interest, all to the power of -12 multiplied by years.
# 7. Multiply the result by the amount of loan entered and you have a monthly payment.
# 8. Print the monthly payment amount.

print ("Program 2 - Car Loan Calculator:")
print ("")
# Define Variables
import math
amount = float(input("Please enter the amount of loan: "))
interest = float(input("Please enter the interest rate (%): "))
years = float(input("Please enter the number of years: "))

# Perform Calculations
rate = (interest / 1200)
n = -12 * years
x = math.pow((1 + rate),n)
monthly_payment = (rate / (1 - x)) * amount

# Output Results
print ("")
print ("The monthly payment based on these values will be ${:.2f}.".format(monthly_payment))