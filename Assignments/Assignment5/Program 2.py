"""
Design and develop a program that presents the user with a multiple choice quiz, built from questions and answers read from a specifically-formatted file.

Begin by designing your solution to this problem in pseudocode, which will be submitted along with the program. Your solution should demonstrate an understanding of how to apply file I/O, list and looping concepts. Your program should be capable of producing a quiz from any text file that uses the following format for each set of question & answers:
<question text>,<answer A text>,<answer B text>,<answer C text>,<answer D text>,<correct answer indicator>
In other words, each line of the quiz file will contain 6 elements: the first is the question text, the 2nd through 5th contain the answer text for the four possible multiple choice answers, and the last element contains a letter or number indicating which of the potential answers is the correct one. The answer text in quiz file should not contain the letters/numbers used to identify each answer to the user when the quiz is being taken.
Examples of quiz file format:
•	What is 2 * 2?,4,2,8,6,A
•	What is capital of Canada?,Toronto,Ottawa,Pennsylvania,The Moon,B
When the quiz program is run, the user will be posed each question in turn, be presented with a lettered ranking of all four possible answers, and then be prompted to enter their choice of answer. Only valid answers (a,b,c,d or 1,2,3,4) should be accepted as valid answers before proceeding to the next question. If an invalid answer choice is entered, a message indicating an invalid choice should be displayed, and the user should be prompted to enter a new choice.
When the program has displayed all questions contained in the file, and received an answer for each, a final score will be calculated and displayed to the user, including both fractional and percentage values. Ex. Your score is 4/5 (80%).
Pseudocode:
1: Read the quiz.csv file.
2: Print out the lines for each row using a range.
3: Format each answer so there is the a,b,c,d value and a space.
4: Have the user enter their choice for the question.
5: Store each choice into an array.
6: Calculate the percentage by using a total variable and a score variable to keep track of correct answers.
7: Display the users score.
"""
#Imports
import csv

# Variables
answer = []
score = 0
total = 0
percentage = 0

# Open a CSV File
with open('quiz.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    # Read each line
    for row in readCSV:
        print (row[0])
        for i in range (1, 5):
            print ("{}) {}".format(chr(i+96),row[i]))
        answer.append(input("Enter choice (a-d): "))
        print ()
        if answer[total].lower() == row[5].lower():
            score += 1
        total += 1
    percentage = (score / total) * 100
    print ("Your score is: {}/{} ({:.0f}%) ".format(score,total,percentage))
