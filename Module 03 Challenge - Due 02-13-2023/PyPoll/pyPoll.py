import os
import csv

pyPollcsv = os.path.join("Resources", "election_data.csv")
#print(pyPollcsv)
#create the oupath for the text file
outpath = os.path.join("Resources", "election_data.txt")
#print(outpath)
#outpath appears good

# I have my pathway open to election data csv
# I need my total votes to begin at 0
totalVotes = 0

# i also need the vote count for each candidate to begin at xero
charlesVote = 0
dianaVote = 0
raymondVote = 0

#the winner count needs to be set to zero
winner = 0
#winning percentage also needs to be set at zero
winPer = 0
#winning candidate should be set to zero
winCan = 0

#I need my reader open
with open(pyPollcsv) as file:
    csvreader = csv.reader(file, delimiter=",")
    next(csvreader) # no headers

    # I have my path established and my reader my the header ready
    # a for loop to check the data 
    for row in csvreader:

            totalVotes +=1 
            candidateName = row[2]
        #this will add the votes together
        #this should grab the candidate names as well

        #now I need to know the cancdidates seperately
            if candidateName == "Charles Casper Stockham":
                charlesVote += 1
            elif candidateName == "Diana DeGette":
                dianaVote +=1
            elif candidateName == "Raymon Anthony Doane":
                raymondVote += 1
            else:
                print(f"the came of the candidate {candidateName} is unknown")

            #ok this should add the votes for each person individually

    #now I need to know what percentage each person got of the total vote
    charlesPer = (charlesVote/totalVotes)*100
    dianaPer = (dianaVote/totalVotes)*100
    raymondPer = (raymondVote/totalVotes)*100

    #now i need a loop to compare teh precentages 
    # the loop checks to see which vote is the greaters and to assign the winCan category

    if dianaVote > winner:
        winner = dianaVote
        winPer = dianaPer
        winCan = "Diana DeGette"
    elif charlesVote > winner:
        winner = charlesVote
        winPer = charlesPer
        winCan = "Charles Casper Stockham"
    elif raymondVote > winner:
        winner = raymondVote
        winPer = raymondPer
        winCan = "Raymond Anthony Doane"

# Im gonna check my if statements worked
# everytime i do the float points, the strings become messed up
# so i broke up the per and votes with quotes
#also the print(f"") string function would not work so I did the strings the long way

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(totalVotes))
print("------------------------------")
print("Charles Casper Stockham: " + "Per: " + str(charlesPer) + "Count: " + (str(charlesVote)))
print("Diana DeGette: " + "Per: " + str(dianaPer) + "Count: " + str(dianaVote))
print("Raymond Anthony Doane: " + "Per: " + str(raymondPer) + "Count: " + str(raymondVote))
print("----------------------------")
print("Winner: " + str(winCan))
print("------------------------------")

# my numnbers appear to match what they should

# ok everything is checking out besides the weird syntax
# im going to do the .write() function to send it to a txt file
#the text file appears to check out fine

with open(outpath, "w") as txtFile:
    txtFile.write("Election Results")
    txtFile.write("\n-------------------------")
    txtFile.write("\nTotal Votes: " + str(totalVotes))
    txtFile.write("\n------------------------------")
    txtFile.write("\nCharles Casper Stockham: " + "Per: " + str(charlesPer) + "Count: " + (str(charlesVote)))
    txtFile.write("\nDiana DeGette: " + "Per: " + str(dianaPer) + "Count: " + str(dianaVote))
    txtFile.write("\nRaymond Anthony Doane: " + "Per: " + str(raymondPer) + "Count: " + str(raymondVote))
    txtFile.write("\n----------------------------")
    txtFile.write("\nWinner: " + str(winCan))
    txtFile.write("\n------------------------------")

