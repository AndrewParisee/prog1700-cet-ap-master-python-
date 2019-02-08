"""
Program 2 - Vowel Counter:
Design and write a program that counts the occurrences of each vowel in any user-entered sentence or phrase.
Your solution should demonstrate an understanding of how to apply list and looping concepts in a program that should:
•	Take a sentence or phrase as input,
•	Count the number of occurrences of each vowel in the user-entered sentence, regardless of case sensitivity,
•	Display the counts per vowel to the user,
•	The program will keep asking the user to enter a new sentence until the user enters the command ‘quit’.
"""
print ("Program 2 - Vowel Counter:")
print ("-----------------------------------")
# Define Variables
phrase_list = [""]
new_phrase = ""

# Perform Calculations
while True:
    print ("")
    new_phrase = input("Type a Phrase (Or Quit To Exit Program): ")
    if new_phrase.lower() == "quit":
        print ("")
        print ("Very Well!")
        quit()
    lower = str.lower(new_phrase)
    convert = list(lower)
    # Count Vowels in the phrase
    a = convert.count("a")
    e = convert.count("e")
    i = convert.count("i")
    o = convert.count("o")
    u = convert.count("u")

# Prints Results
    print ("")
    print ("Letter A count: {}".format(a))
    print ("Letter E count: {}".format(e))
    print ("Letter I count: {}".format(i))
    print ("Letter O count: {}".format(o))
    print ("Letter U count: {}".format(u))