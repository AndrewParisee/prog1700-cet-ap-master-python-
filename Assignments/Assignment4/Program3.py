"""
Program 3 - Election:
An election is approaching and Elections Head Office wants a program to print a candidate list,
including who won the election, and who came in last place (in order to laugh at them).

Your solution should demonstrate an understanding of how to apply list/loop concepts in a program that should:
•	Ask the user how many candidates are running in the current election,
•	For each numbered candidate up to the user-entered count of candidates,
    allow the user to enter a name and the number of votes that person received.
•	Calculate and output a list of all candidate names,
•	Display what share of the total vote, as a percentage, that each candidate won,
•	Highlight the candidate(s) with highest and lowest vote counts.
(Hint: Some potential solution ideas: Research parallel arrays or two-dimensional lists)
"""
print ("Program 3 - Election:")
print ("-----------------------------------------------")
# Define Variables
number_of_candidates = 0
number_of_votes = 0
i = 0
candidate = []
votes = []
votes_total = 0

# Perform Calculations
while True:
    try:
        number_of_candidates = int(input("Enter the Number of Candidates in the Election: "))


# Input Each Candidate and Number of Votes
        for i in range(0, number_of_candidates):
            name = input("\nEnter the Name of Candidate #{}: ".format(i + 1))
            candidate.append(name)
            number_of_votes = int(input("Enter the Number of Votes for Candidate {}: ".format(i + 1)))
            votes.append(number_of_votes)
            votes_total = votes_total + number_of_votes

# Determine positions of first and last place
        i = 0
        first_place = votes[0]
        last_place = votes[0]
        for i in range(0, len(votes)):
            if votes[i] > first_place:
                first_place = votes[i]
            if votes[i] < last_place:
                last_place = votes[i]

# Print Results

        print ("Election Results")
        print ("-----------------------------------------------")
        i = 0
        while i < len(candidate):
            percentages = float(votes[i] / votes_total)

            strOut = candidate[i] + '\t\t\t' + " - " + str("{:.1f}".format(percentages * 100)) + "%"
            if votes[i] == first_place:
                strOut = strOut + " <-- First Place"
            if votes[i] == last_place:
                strOut = strOut + " <-- Last Place... HAHAHAHA!"
            print (strOut)
            i += 1
    except ValueError:
        print ("Enter an integer value!")