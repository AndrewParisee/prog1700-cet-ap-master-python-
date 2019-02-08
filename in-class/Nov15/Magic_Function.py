"""
Build an applicatio with a magic function. The function will take in an array as a parameter and will return the
first element in the array for now.

The magic function will find the median value in the array. In a sortd array of numbers the median is the middle value.
If there are an off number of entries the median is the middle value, if even it is the average of the two middle values.
odd -> number % 2 == 1 even -> number % 2 == 0
"""
# Define Variables
import statistics
entered_string = ""
number_list = list()


# Perform Calculations
def magic_function(number_list):
    #For Even
    if len()
    median = statistics.median(number_list)
    return median


while True:
    try:
        entered_string = input("Enter a number (d to quit): ").lower()
        if entered_string.lower() == "d":
            break
        number = int(entered_string)
        number_list.append(number)

    except ValueError:
        print ("Please Enter a Valid Number!\n")
# Print Results
print (number_list)
print ("The median is {}.".format(magic_function(number_list)))