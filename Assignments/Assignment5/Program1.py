"""
Design and write a program that reads the text from a provided text file, displays the text on-screen, makes some alterations to the text and outputs the changed text to the screen, then saves the altered text as a new file.

Begin by designing your solution to this problem in pseudocode, which will be submitted along with the program. Your solution should demonstrate an understanding of how to apply file I/O, list and looping concepts. Your program will read all the text contained in a file (provided) and output the unchanged text content to the console. Your program should then make the following alterations to the original text:
•	Add a line number (starting with line 1) to the beginning of each line of text in the file.
•	Your program should randomly select a line in the text and convert it to all capital letters.
•	Every other line in the text (besides the all-caps version mentioned above) should be converted to all lowercase letters.
Once all text alterations are complete, output the altered text to the console, and finish by saving it as a new text file.
Every time the program is run it should pick a different random line of text and you can assume the file doesn’t contain any commas. Although a text file is provided, your finished program should work with any text-based file, not just the Jed text.
Pseudocode:
1: Read the Jed Input File.
2: Insert lines read from input file into a list.
3: Number each line starting from 1.
4: Import random in a loop to continuously select a random number.
5: In an if statement use the random number to select a line that has each letter capitalized.
6: Have each other line set in lowercase.
7: Display the altered text with the capital lines changing each time the program is run.
8: Write the completed altered text to the Jed Output file.
"""
#Imports
from random import *
# Variables
originalTitle = "--------------------------\nORIGINAL FILE TEXT\n--------------------------"
alteredTitle = "--------------------------\nALTERED FILE TEXT\n--------------------------"
jedLines = []

# Open a file text
fileName = "JedInput"
with open(fileName , 'r') as f:
    lines = f.readlines()

print(originalTitle)
# Read lines in text file
for x in range(0, len(lines)):
    lines[x] = lines[x].strip("\n")
    print(lines[x])
    lines[x] = "{}: {}".format(x + 1, lines[x])

randomInt = randint(0,6)

print("\n{}".format(alteredTitle))
# Random select line to capitalize
for x in range(0, len(lines)):
    if x == randomInt:
        lines[x] = lines[x].upper()
        print(lines[x])
    else:
        lines[x] = lines[x].lower()
        print (lines[x])

# Write to Ouput Text
with open("JedOutput", "w") as f:
    f.writelines("\n".join(lines))