print ("Highest Common Divisor Program:")
print ("")
# Define Variables.
first_number = 0
second_number = 0
replay = ""

# Perform Calculations.
while replay.lower() != "n":
    # HCD Function find thes remainder of first number divided by second.
    def GetHighestCommonDivsor(first_number, second_number):
        while second_number != 0:
            if second_number > first_number:
                return GetHighestCommonDivsor(second_number, first_number)
            x = first_number % second_number
            if x == 0:
                return second_number
            return GetHighestCommonDivsor(x, second_number)

    # If first number is entered incorrectly, they get a chance to enter a valid input.
    while True:
        try:
            first_number = int(input("Enter the first number: "))
            break
        except ValueError:
            print("ERROR! Enter a valid first number.")
    # If second number is entered incorrectly, they get a chance to enter a valid input.
    while True:
        try:
            second_number = int(input("Enter the second number: "))
            break
        except ValueError:
            print("ERROR! Enter a valid second nubmer.")
# Output Results.
    print ("The Highest Common Divisor of {} and {} is {}.".format(first_number,second_number,GetHighestCommonDivsor(first_number,second_number)))
    print ("")
    while True:
        replay = input("Would you like to try again? (y/n)")
        print("")
        if replay.lower() == "y":
            break
        elif replay.lower() == "n":
            print("Thank you for using the Highest Common Divisor Program.")
            break
        else:
            print("")
            print ("Invalid Entry! Please Enter Y or N.")
            print("")