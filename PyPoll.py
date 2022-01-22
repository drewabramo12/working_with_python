# The data we need to retrieve
import os
import csv
    #Assign a variable to election data and open path
file_to_load = os.path.join('Resources', 'election_results.csv')
file_to_save = os.path.join("Analysis","election_analysis.txt")

#1. Initialize a total vote counter.
total_votes = 0
candidate_options =[]
# 1. Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Read and print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        #2. Add to the total vote count.
        total_votes += 1
        # Print the canidate name from each row
        candidate_name=row[2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
        # Add it to the list of candidates.
            candidate_options.append(candidate_name)

         # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] +=1     

    

with open(file_to_save,'w') as txt_file:
    election_results = (
       f"\nElection Results\n"
       f"-------------------------\n"
       f"Total Votes: {total_votes:,}\n"
       f"-------------------------\n")
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
        # If true then set winning_count = votes and winning_percent =
        if (votes > winning_count) and (vote_percentage > winning_percentage):
         # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
        # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}\n"
            f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

