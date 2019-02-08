import csv

current_hitpoints = 0
hitpoints = 0
play = ""

print ("Welcome to the Dungeon Attack application where none shall survive! Simply try to live as long as you can.")
while True:
    try:
        play = input("Hit any key to continue ('Q' or 'q' to quit): ")
        if play.lower() == "q":
            print ("That's It. Retreat in fear and warn your friends!")
            quit(0)
        hitpoints = int(input("\nPlease enter your initial hit points (1-200): "))
        if hitpoints <= 200:
            break
        else:
            print("You do not listen very well do you? Think you are going to survive this dungeon?")
    except ValueError:
        print("You do not listen very well do you? Think you are going to survive this dungeon?")


with open('monsters.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    for row in readCSV:
        #print (row[0])
        current_hitpoints = max(hitpoints - int(row[2]), 0)
        print ("You were attacked by a {} with a {} attack for {} damage. Current hit points: {:.0f}".format(row[0], row[1], row[2], current_hitpoints))
        if current_hitpoints == 0:
            print("That was sad. And brief. At least the elf feels better about himself!!!\n")
            break