#Imports
import RPi.GPIO as GPIO
import time

#Variables
tap_code_list = []


#2d list for tap code
tap_code_list.append(["A","B","C/K","D","E"])
tap_code_list.append(["F","G","H","I","J"])
tap_code_list.append(["L","M","N","O","P"])
tap_code_list.append(["Q","R","S","T","U"])
tap_code_list.append(["V","W","X","Y","Z"])

#GPIO Interface
ledPin=17
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin,GPIO.OUT)

#Tap Code Method
def SendMessageViaTapCode(sentMsg):
    for letter in sentMsg:
        for row_index in range(len(tap_code_list)):
            row = tap_code_list[row_index]
            for col_index in range(len(row)):
                if letter.upper() == 'K':
                    letter = 'C'
                if tap_code_list[row_index][col_index][0] == letter.upper():
                    Tap(row_index + 1, col_index + 1)
                    time.sleep(1)
                elif letter.upper() == " ":
                    time.sleep(1.5)

    return

# Tap Method to make the led flash on the breadboard
def Tap(row_index, col_index):
    for i in range(row_index):
        GPIO.output(ledPin, 1)
        time.sleep(0.2)
        GPIO.output(ledPin, 0)
        time.sleep(0.2)

    time.sleep(0.5)

    for i in range(col_index):
        GPIO.output(ledPin, 1)
        time.sleep(0.2)
        GPIO.output(ledPin, 0)
        time.sleep(0.2)

    time.sleep(0.5)