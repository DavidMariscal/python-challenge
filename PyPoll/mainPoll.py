import os
import csv
import statistics

# Upload data from the PyPoll csv file
election_data_csv = os.path.join('Election_data.csv')
 

# Initialize variables
row = []
total_votes = []
total_number_of_votes = 0
correy_votes = 0
khan_votes = 0
li_votes = 0
otooley_votes = 0
correy_percent = 0.0
kahn_percent = 0.0
li_votes = 0.0
otooley_percent = 0.0

with open(election_data_csv, 'r') as csvfile:    

    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip header 
    csv_header = next(csvfile)

    # Read each row of data
    for row in csvreader:
        
        # Calculate total number of votes cast in the election
        
        total_votes.append(row[0])
        total_number_of_votes = len(total_votes)
        
        if (row[2] == "Correy"):
            correy_votes += 1
        elif (row[2] == "Khan"):
            khan_votes += 1
        elif (row[2] == "Li"):
            li_votes += 1
        else:
            otooley_votes += 1
            
    # Calculate percentage of votes in order to know who won
    kahn_percent = khan_votes / total_number_of_votes
    correy_percent = correy_votes / total_number_of_votes
    li_percent = li_votes / total_number_of_votes
    otooley_percent = otooley_votes / total_number_of_votes 
    
   # Calculate winner of the election 
    if khan_votes > correy_votes:
       winner = "Khan"
    elif correy_votes > li_votes:
       winner = "Correy"
    elif li_votes > otooley_votes:
       winner = "Li"
    else:
       winner = "O'Tooley"


# Print Stats
print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {total_number_of_votes}")
print(f"---------------------------")
print(f"Kahn: {kahn_percent:.3%}({khan_votes})")
print(f"Correy: {correy_percent:.3%}({correy_votes})")
print(f"Li: {li_percent:.3%}({li_votes})")
print(f"O'Tooley: {otooley_percent:.3%}({otooley_votes})")
print(f"---------------------------")
print(f"Winner: {winner}")
print(f"---------------------------")

# Specify File To get the stastistics output
output_file = os.path.join('election_statistics_output.txt')

with open(output_file, 'w',) as txtfile:

# Output to txt file
    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {total_number_of_votes}\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Kahn: {kahn_percent:.3%}({khan_votes})\n")
    txtfile.write(f"Correy: {correy_percent:.3%}({correy_votes})\n")
    txtfile.write(f"Li: {li_percent:.3%}({li_votes})\n")
    txtfile.write(f"O'Tooley: {otooley_percent:.3%}({otooley_votes})\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write(f"---------------------------\n")
