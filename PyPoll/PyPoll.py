# Assign the Variables

total_votes = 0                      # will count all the votes
candidate_votes = {}                 # will create a dictionary that contains candidate name and vote count per candidate


# read in the csv data file

csvpath = os.path.join("election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_headers = next(csvreader)
    
        
    # iterate through the file and collect the data   
    for row in csvreader: 
        total_votes = total_votes + 1       # adds to the total vote count
        candidate_name = row[2]             # gets the candidate name from each row 
        
        # create the candidate name list and see if they are already in the dictionary
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1
            
print("Election Results")
print("-----------------------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------------------")

for candidate, votes in candidate_votes.items():      # Get the percentage votes each candidate recieved and print results
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}%  {votes}")
    
    
winner = ''
max_votes = 0

for candidate, votes in candidate_votes.items():      # Find the winning candidate and print the name
        if votes > max_votes:
            max_votes = votes
            winner = candidate

print("-----------------------------------------")
print(winner)


# Write the results to a txt file


csvoutput = os.path.join("election_analysis.txt")

with open(csvoutput, 'w') as file:
        file.write("Election Results  \n")
        file.write("-----------------------------------------  \n")
        file.write(f"Total Votes: {total_votes}  \n")
        file.write("-----------------------------------------  \n")
        file.write(f"{candidate}: {percentage:.3f}%  {votes}  \n")
        file.write("-----------------------------------------  \n")
        file.write("Winner: (winner)  \n")

