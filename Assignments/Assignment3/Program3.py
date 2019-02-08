# Program 3 - Tax Schedule:
# You will write a program that computes taxes according to the following schedule:
#  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
# |If your status is 'Single' and if       |       but not over      |       the tax is        |    of the amount over|
# |   the taxable income is over           |                         |                         |                      |
# |              $0                        |          $8,000         |           10%           |            $0        |
# |            $8,000                      |         $32,000         |       $800 + 15%        |          $8,000      |
# |           $32,000                      |                         |      $4,400 + 25%       |         $32,000      |
#  -------------------------------------------------------------------------------------------------------------------
# |If your status is 'Married' and         |       but not over      |       the tax is        |    of the amount over|
# | if the taxable income is over          |                         |                         |                      |
# |              $0                        |        $16,000          |          10%            |          $0          |
# |           $16,000                      |        $64,000          |     $1,600 + 15%        |       $16,000        |
# |           $64,000                      |                         |     $8,800 + 25%        |       $64,000        |
#  -------------------------------------------------------------------------------------------------------------------
# First, create a flowchart that clearly shows all of the paths of execution that will exist within your designed
# solution to this problem. Then, write a console application that will input the marital status and taxable income
# and then output the corresponding total tax.
print ("Program 3 - Tax Schedule")
print ("")
# Define Variables
status = input("Enter your Marital Status: ").upper()
income = int(input("Enter your Taxable Income: "))
income_tax = 0

# Perform Calculations
if status == "single".upper():
    if income <= 8000:
        income_tax = income * 0.10
    elif income > 8000 and income <= 32000:
        income_tax = 800 + ((income - 8000) * 0.15)
    elif income > 32000:
        income_tax = 4400 + ((income - 32000) * 0.25)
elif status == "married".upper():
    if income <= 16000:
        income_tax = income * 0.10
    elif income > 16000 and income <= 64000:
        income_tax = 1600 + ((income - 16000) * 0.15)
    elif income > 64000:
        income_tax = 8800 + ((income - 64000) * 0.25)

# Print Results
print ("")
print ("Your Total Tax is ${:.2f}".format(income_tax))
