# working_with_python

## Overview if Election Audit

The purpose of this audit was to break down the turn out from each county. This was broken into four parts.

1.  Collection of counties that participated in the election.
2. The count of voters from each county that participated in the election.
3. Retrieval of the percentage of votes across in each county compared to all votes documented.
4. Determination of the county with the highest voter turn out.

As a note, all other code reflected in the PyPoll_challenge_starter_code.py was on the file before working with it. Values to determine total votes, candidate names, votes, percentages, and the popular vote were already provided.

## Resources
-Data Source: election_results.csv
-Software: Python 3.9.7, Visual Studio Code: 1.63.2

## Results
The analysis of the county election data:
- There were "369,711" votes cast in this election.

This was determined by creating the `for` loop:
```
for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1
```
- The counties were:
    - Arapahoe
    - Denver
    - Jefferson
This was determined by creating the `for` loop:
```
for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]
```
- The county turn out was:
    - Jefferson had 10.5% of the total votes with 38,855 votes.
    - Denver had 82.8% of the total votes with 306,055 votes.
    - Arapahoe had 6.7% of the total votes with 24,801 votes.
- The county with the largest turn out was:
    - Denver, which had 306,055 votes 82.8% of the total votes.
- The candidate's votes received were:
    - Charles Casper Stockham: had 23.0% of the total votes with 85,213 votes.
    - Diana DeGette had 73.8% of the total votes with 272,892 votes.
    - Raymon Anthony Doane had 3.1% of the total votes with 11,606 votes.

## Election-Audit Summary



