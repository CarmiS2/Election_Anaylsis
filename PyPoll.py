# The data we need to retrieve. 
# 1. The total number of votes cast 
# 2. A complete list of candidates who received votes 
# 3. The Precentage of votes each candidate won 
# 4. The total number of votes each candidate won 
# 5. The winner of the elecation based on popular vote.

# add our dependecies 
import csv 
import os 
# Assign a variable to load a file from a path
file_to_load = os.path.join("Resource", "election_results.csv")
#assign a variable to save the file to a path 
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open the elecation results and read the file 
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

#read adn print the header row  
    headers = next(file_reader)
    print(headers)
