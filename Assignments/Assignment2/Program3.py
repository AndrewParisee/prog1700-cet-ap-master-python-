# Program 3 - Imperial to Metric Conversion
# Write a console program that converts a distance given in miles, yards, feet,
# and inches to the metric equivalent length in kilometres, metres, and centimetres.
# Begin by designing your solution to this problem in pseudocode, which will be
# submitted along with the program.
#
# After the numbers of miles, yards, feet, and inches are input by the user, the
# length should be converted entirely into inches and then divided by 39.37 to obtain
# the value in metres. The Python int function should be used to break the total number
# of metres into a whole number of kilometres and metres. The number of centimetres
# should be displayed to one decimal place.
#
# Required Formulas:
# total inches = 63360 * miles + 36 * yards + 12 * feet + inches
# total metres = total inches / 39.37
# kilometres = Int(metres/1000)
# Pseudocode:
# 1. Define miles, yards, feet, and inches as input variables.
# 2. Calculate the total inches of each of the previous values entered.
# 3. Calculate the total metres and the total centimetres.
# 4. Use the total metres to calculate the kilometres.
# 5. Use the total metres and total centimetres to determine the metres and centimetres.
# 6. Print the metric conversions using the calculated variables.

print ("Program 3 - Imperial to Metric Conversion")
print ("")
# Define Variables
miles = float(input("Enter the number of miles: "))
yards = float(input("Enter the number of yards: "))
feet = float(input("Enter the number of feet: "))
inches = float(input("Enter the number of inches: "))

# Perform Calculations
total_inches = 63360 * miles + 36 * yards + 12 * feet + inches
total_metres = total_inches / 39.37
total_centimetres = total_metres * 100
kilometres = int(total_metres / 1000)
metres = int(total_metres % 1000)
centimetres = float(total_centimetres % 100)

# Output Results
print ("")
print ("The metric length is:")
print ("- {:.1f}".format(kilometres) + " kilometres.")
print ("- {:.1f}".format(metres) + " metres.")
print ("- {:.1f}".format(centimetres) + " centimetres.")
