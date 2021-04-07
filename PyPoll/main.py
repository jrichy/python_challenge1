

import os
import csv

#  set the path for the CSV file 

PyPollcsv = os.path.join("Resources","election_data.csv")

#  set variables

count = 0
candidateList = []
uniqueCandidate = []
votePercent = []
voteCount = []
# Open the CSV 

with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    for row in csvreader:
        
        count = count + 1
        candidateList.append(row[2])
        # set the candidatelist to get the unique candidate names
    for x in set(candidateList):
        uniqueCandidate.append(x)
        y = candidateList.count(x)
        voteCount.append(y)
        z = (y/count)*100
        votePercent.append(z)
        
    winningVoteCount = max(voteCount)
    winner = uniqueCandidate[voteCount.index(winningVoteCount)]
    
#code
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(uniqueCandidate)):
            print(uniqueCandidate[i] + ": " + str(votePercent[i]) +"% (" + str(voteCount[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")

# Print to a text file: election_results.txt
with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(uniqueCandidate))):
        text.write(uniqueCandidate[i] + ": " + str(votePercent[i]) +"% (" + str(voteCount[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")
