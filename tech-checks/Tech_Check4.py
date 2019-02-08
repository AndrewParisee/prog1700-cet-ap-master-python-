# Define Variables
correct_input = 1  # ERROR, not changing the incorrect input to be greater than 1

letter_entered = ""
user_input = ""
sign_entered = ""
number_output = 0

value_letters = ["A", "B", "C", "D", "E", "F"]
value_signs = ["+", "-", ""]

# Perform Calculations
while letter_entered not in value_letters or sign_entered not in value_signs:
    if correct_input == 1:  # ERROR, equal was added to error of displaying enter valid letter grade.
        user_input = input("Enter a letter grade: ").upper()

        print ("You must enter a valid letter grade!")



    if user_input != "" and len(user_input) <= 2:
        letter_entered = user_input[0]
        if len(user_input) == 2 and letter_entered != "F":
            sign_entered = user_input[1]
        elif len(user_input) == 2:
            sign_entered = "x"
        else:
            sign_entered = ""

        correct_input == correct_input ++ 1

if letter_entered == "A":
    number_output += 4
elif letter_entered == "B":
    number_output += 3
elif letter_entered == "C":
    number_output += 2
elif letter_entered == "D":
    number_output += 1

if sign_entered == "+" and letter_entered != "A":
    number_output += 0.3
elif sign_entered == "-":
    number_output -= 0.3

# Print Results
print("The Numeric Value is {:.1f}".format(
    number_output))  # ERROR, the decimal place was set to display the number without a decimal place.
