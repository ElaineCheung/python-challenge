
import csv
import os


csvpath = os.path.join("Resources", "election_data.csv")


#The total number of votes cast

Total_votes = []
counter = 1
with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        Total_votes = counter

with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    Total_votes = sum(int(counter) for row in csvreader)
print(Total_votes)


# A complete list of candidates who received votes
Candidate_list=[]

with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        if row[2] not in Candidate_list: 
            Candidate_list.append(row[2])
print(Candidate_list)


Khan_votes = []

with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    Khan_votes = sum(int((row[2]).count("Khan")) for row in csvreader) 
    
Khan_percent=(Khan_votes/Total_votes)
Khan_percentage="{:.2%}".format(Khan_percent)
print(Khan_votes)
print(Khan_percentage)



Correy_votes = []

with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    Correy_votes = sum(int((row[2]).count("Correy")) for row in csvreader) 

Correy_percent=(Correy_votes/Total_votes)
Correy_percentage="{:.2%}".format(Correy_percent)
print(Correy_votes)
print(Correy_percentage)


Li_votes = []

with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    Li_votes = sum(int((row[2]).count("Li")) for row in csvreader) 

Li_percent=(Li_votes/Total_votes)
Li_percentage="{:.2%}".format(Li_percent)
print(Li_votes)
print(Li_percentage)



OTooley_votes = []

with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    OTooley_votes = sum(int((row[2]).count("O'Tooley")) for row in csvreader) 

OTooley_percent=(OTooley_votes/Total_votes)
OTooley_percentage="{:.2%}".format(OTooley_percent)
print(OTooley_votes)
print(OTooley_percentage)




#The winner of the election based on popular vote.
votes_per_candidate = {"Khan":Khan_votes, "Correy": Correy_votes, "Li": Li_votes, "O'Tooley": OTooley_votes}
import operator
winner=max(votes_per_candidate.items(), key=operator.itemgetter(1))[0]
print(winner)



output = (
    f"\nElection Results\n"
    f"-----------------\n"
    f"Total Votes: {Total_votes}\n"
    f"-----------------\n"
    f"Khan: {Khan_percentage} ({Khan_votes})\n"
    f"Correy: {Correy_percentage} ({Correy_votes})\n"
    f"Li: {Li_percentage} ({Li_votes})\n"
    f"O'Tooley: {OTooley_percentage} ({OTooley_votes})\n"
    f"-----------------\n"
    f"Winner: {winner}\n"
    f"-----------------\n")

# Print all of the results (to terminal)
print(output)

file_to_output = os.path.join("analysis", "PyPoll_output.txt")

# Save the results to analysis text file
with open(file_to_output, "a") as txt_file:
    txt_file.write(output)




