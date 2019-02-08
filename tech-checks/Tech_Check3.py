# PROG 1700 Tech Check #3 Variables, Operators, Inputs and Output
print ("Tax Withholding Calculator")
print ("")

# Define Variables
weekly_salary = int(input("Please enter the full amount of your weekly salary: $"))
dependants = int(input("How many dependants do you have?: "))
Provincial_Tax = 0.06
Federal_Tax = 0.25
Dependant_Tax = 0.02
prov_tax = ""
fed_tax = ""
dep_deduction = ""

# Perform Calculations
prov_tax = weekly_salary * Provincial_Tax
fed_tax = weekly_salary * Federal_Tax
dep_deduction = weekly_salary * Dependant_Tax * dependants
Total_Withheld = (prov_tax - dep_deduction) + fed_tax
Take_Home = weekly_salary - Total_Withheld

# Output Results
print ("")
print ("Your Provincial Tax Withheld is ${:.2f}.".format(prov_tax))
print ("Your Federal Tax Withheld is ${:.2f}.".format(fed_tax))
print ("Your Dependant Deduction for {}".format(dependants) + " dependants is ${:.2f}.".format(dep_deduction))
print ("The Total Amount Withheld is ${:.2f}.".format(Total_Withheld))
print ("Your Total Take-Home Pay is ${:.2f}.".format(Take_Home))