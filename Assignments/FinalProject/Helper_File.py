#Imports
from Morse_Code_File import *
from Tap_Code_File import *

#Variables
userMessage = ""
welcomeMessageString = "Welcome to the Code Sender Application!"
sendMessageString = "Would you like to send a message? (y/n): "
invalidInputString = "Invalid input.\n"



#Functions


#Choice Method
def TapOrMorse(sentMsg):
    while True:
        msgMedium = raw_input("Would you like to send your message with Tap or Morse code? (t/m): ").lower()
        if msgMedium.lower() == "t":
            print("[Message is sent using Tap Code with LED]\n")
            SendMessageViaTapCode(sentMsg)
            break
        elif msgMedium.lower() == "m":
            print("[Message is sent using Morse Code with LED]\n")
            SendMessageViaMorseCode(sentMsg)
            break
        else:
            print ("")
    return

#User Input Method
def ReadMessageFromUserInput():
    return raw_input("Enter your message: ")

#Read Message From File Method
def ReadMessageFromFile():
    fileMessage = ""
    try:
        inputFile = raw_input("Enter the file path and name: ")
        with open(inputFile, 'r') as f:
            lines = f.readlines()
        for x in range(0, len(lines)):
            fileMessage += lines[x]
        return fileMessage
    except:
        print("Problem Loading File\n")
    return