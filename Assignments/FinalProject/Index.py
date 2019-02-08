#Imports
from Helper_File import *

#Variables
message = ""

#Beginning of the Code
print(welcomeMessageString)

#While Loop to Run Code
while True:
    try:
        message = raw_input(sendMessageString).lower()
        if message.lower() == "y":
            while True:
                msgType = raw_input("Would you like to send a typed message or loaded from file? (t/f): ").lower()
                if msgType.lower() == "t":
                    userMessage = ReadMessageFromUserInput()
                elif msgType.lower() == "f":
                    userMessage = ReadMessageFromFile()
                else:
                    print(invalidInputString)

                if len(userMessage) > 0:
                    TapOrMorse(userMessage)
                    userMessage = ""
                    break

        elif message.lower() == "n":
            print("Application Ended")
            break
        else:
            print(invalidInputString)

    except:
        print("Error! Unexpected Value Entered!\n")