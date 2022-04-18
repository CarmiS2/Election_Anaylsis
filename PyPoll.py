# add our dependecies 
import csv 
import os 
# Assign a variable to load a file from a path
file_to_load = os.path.join("Resource", "election_results.csv")
#assign a variable to save the file to a path 
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. initilize a total vote counter. 
total_votes = 0
#Candidate Options 
candidate_options = []
# 1. declare the empty dictionary 
candidate_votes = {} 

#winnign candidate and winning coutn tracker 
winning_candidate = ""
winning_count = 0 
winning_percentage = 0 

#open the elecation results and read the file 
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #read the header row  
    headers = next(file_reader)
    for row in file_reader:
        total_votes += 1

        #print teh candidate naem from each row 
        candidate_name = row[2]
        # if the candidate does nto amth any existing candidate... 
        if candidate_name not in candidate_options:
            #add it to the list of canidates. 
            candidate_options.append(candidate_name)
            # 2. begin tracking that candidate's vote count 
            candidate_votes[candidate_name] = 0
            # add a vote to that candidate's count. 
        candidate_votes[candidate_name] += 1
with open(file_to_save, "w") as txt_file:
        #pritn the final vote count to the terminal 
    election_results = (
        f"\nElection Results\n"
        f"------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------\n")
    print(election_results, end="")
    #save the final vote count to the text file 
    txt_file.write(election_results)

    #determine the percentage of votes for each candidate by looping through the counts 
    #1. iterate through the candidate list. 
    for candidate_name in candidate_votes:
        #2. retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # 3. calculate the percentage of votes. 
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. print the canidate name and precentage of votes 
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # print each candidates voter count and percentage to the terminal
        print(candidate_results)
        # save the candidate results to our text file
        txt_file.write(candidate_results)
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # if true then set winning_count = votes and winning_precent =
            # vote_percentage 
            winning_count = votes 
            winning_percentage = vote_percentage
            #and set the winning_candidate equal to the canidates name 
            winning_candidate = candidate_name
    # to do: print out the winning candidate, vote count adn orecentage to 
    # terminal 
    winning_candidate_summary = (
        f"---------------\n"
        f"winner: {winning_candidate}\n"
        f"winning vote count: {winning_count: ,}\n"
        f"winning percentage: {winning_percentage:.1f}%\n"
        f"---------------\n")
    print(winning_candidate_summary)
# save the winning candidates results to the test file 
    txt_file.write(winning_candidate_summary)

# 1. The total number of votes cast 
# 2. A complete list of candidates who received votes 
# 3. The Precentage of votes each candidate won 
# 4. The total number of votes each candidate won 
# 5. The winner of the elecation based on popular vote.
