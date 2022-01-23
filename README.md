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

![election_analysis](https://github.com/drewabramo12/working_with_python/blob/main/Analysis/election_analysis.txt)


- There were "369,711" votes cast in this election.
- The counties were:
    - Arapahoe
    - Denver
    - Jefferson
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

### Results Explanation

The analysis occurred through a structure of two different `with open()` codes. The first `with open()` opened and read the election_results.csv and was used to populate the total_votes, candidate_name, candidate_options, candidate_votes, county_name, county and county_votes variables through one `for` loop. The second `with open()` used these populated variables to run two `for` loops as well as write the results into the election_analysis.txt file. The first `for` loop printed the county name, percentage of overall votes and count of votes. It also determined which county had the highest turn out. All of this was written into the election_analysis.txt file. The second `for` loop was used to create a similar pattern to determine each candidate's percentage of overall vote and who was the winner of the election. Some lines of code that are worth noting are the lines:
```
        cvote_percentage = float(cvotes) / float(total_votes) * 100
        county_results = (f"{county_name}: {cvote_percentage:.1f}% ({cvotes:,})\n")
```
These lines of code allowed for the creation of a variable that stores the percentage of the county vote and could be used elssewhere rather than needing to use the same algorithm over and over. It also formats the county result information into an easily printable string that works with its `for` loop.

## Election-Audit Summary

This created script could be very useful other local elections of this scale across the united state. It is very flexible in its output and can contain multiple extra counties and candidates without any loss of fidelity of analysis. This script could also be modified to scale with the size of the election. A mayoral election would just need to change the county variables and printables to reflect city districts instead. Another relevant modification that may not reflect on a singular election result but also future elections may be to look at including censor information to get a percentage of turn out for each county compared to county population. This information could be used to help get a better idea about civil engagement within the county and can help justify initiative for local community out reach for better representation.