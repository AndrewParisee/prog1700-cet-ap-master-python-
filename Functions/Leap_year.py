def is_leap_year(year):
    is_leap = False

    if entered_year % 4 == 0 and entered_year % 100 != 0:
        is_leap = True
    elif entered_year % 400 == 0:
        is_leap = True
    else:
        is_leap = False

    return is_leap

# Enter 1900, 2000, 2008, 2017
# for steps in range(4):
entered_year = int(input("Please enter a year(-1 to quit): "))

while(entered_year != -1):
    if (is_leap_year(entered_year)):
      print ("Is a leap year!")
    else:
       print ("Not a leap year!")
    print("")
    entered_year = int(input("Please enter a year(-1 to quit): "))

print ("End of Program!")
