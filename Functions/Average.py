# Define Variables
def get_average(num1,num2,num3):
    average = 0

    # HIDDEN MAGIC
    my_sum = num1 + num2 + num3
    average = my_sum / 3

    return average

number_one = int(input("Please enter the first number: "))
number_two = int(input("Please enter the second number: "))
number_three = int(input("Please enter the third number: "))

my_average = get_average(number_one,number_two,number_three)

# Display Results
print ("The average is: {:.1f}".format(my_average))
