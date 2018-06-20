import os
import csv

election_dataCSV = os.path.join("PyPoll", "Resources", "election_data.csv")

# EXAMPLE
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------

with open(election_dataCSV, 'r') as csvfile:

    # Pass over header
    csv_header = next(csvreader)

    # initialize variables to zero
    total_votes = 0
    percent_votes = total_votes
    Khan_votes = 0
    Khan_percent = 0
    Correy_votes = 0
    Correy_percent = 0
    Li_votes = 0
    Li_percent = 0
    OTooley_votes = 0
    OTooley_percent = 0
    current_max_votes = 0
    most_votes = 0

    # Loop through data
    for row in csvreader:
        total_votes += 1
        Khan_votes += str("Khan")
        Khan_percent = (Khan_votes / total_votes) *100
        Correy_votes += str("Correy")
        Correy_percent = (Correy_votes / total_votes) *100
        Li_votes += str("Li")
        Li_votes = (Li_votes / total_votes) * 100
        OTooley_votes += str("O'Tooley")
        OTooley_percent = (OTooley_votes / total_votes) * 100
        for max_votes in total_votes:
            if current_max_votes > max_votes:
                current_max_votes = winner    
        
    #Print out data
    print("Election Results")
    print("___________________")
    print(f"Total Votes: {str(total_votes)}")
    print("___________________")
    print(f"Khan: {str(percent_votes, (Khan_votes))}")
    print(f"Li: {str(percent_votes, (Li_votes))}")
    print(f"Correy: {str(percent_votes, (Correy_votes))}")
    print(f"O'Tooley: {str(percent_votes, (OTooley_votes))}")
    print("___________________")
    print(f"Winner: {str(most_votes)}")


