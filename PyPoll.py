# The data we need to retrieve
import os
import csv
    #Assign a variable to election data and open path
file_to_load = os.path.join('Resources', 'election_results.csv')
file_to_save = os.path.join("Analysis","election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
 
# Use the open statement to open the file as a text file

with open(file_to_save,'w') as txt_file:
#Write three counties to the file.
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")



#1. The total number of votes cast

#2. A complete list of candidates who received votes

#3. The percentage of votes each candidate won

#4. The total number of votes each candidate won

#5. The winner of the election results