# Variables and Input
first_filling = 23352
second_filling = 23695
gas_consumed = 14

# Processing
gas_mileage = (second_filling - first_filling) / gas_consumed

# Output
print ("The gas mileage is: {:.2f} miles per gallon.".format(gas_mileage))