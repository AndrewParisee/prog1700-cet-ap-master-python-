# The following code has been adapted from "Physical computing with Raspberry Pi".
# The code can be found on the following website.
# https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/morse_code/

#Imports
import RPi.GPIO as GPIO
import time



#Morse Code Dictionary
CODE = {' ': ' ',
        "'": '.----.',
        '(': '-.--.-',
        ')': '-.--.-',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ':': '---...',
        ';': '-.-.-.',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-'}

#GPIO Interface
ledPin=17
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin,GPIO.OUT)


#Dot Method for Morse Code
def dot():
   GPIO.output(ledPin,1)
   time.sleep(0.2)
   GPIO.output(ledPin,0)
   time.sleep(0.2)

#Dash Method for Morse Code
def dash():
   GPIO.output(ledPin,1)
   time.sleep(0.5)
   GPIO.output(ledPin,0)
   time.sleep(0.2)


# Morse Code Method
def SendMessageViaMorseCode(sentMsg):
    for letter in sentMsg:
        for symbol in CODE[letter.upper()]:
            if symbol == '-':
                dash()
            elif symbol == '.':
                dot()
            else:
                time.sleep(0.5)
        time.sleep(0.5)
    return