# importing dependencies
import csv
import os
import math 

# get csv path
from pathlib import Path
filepath = Path("C:\\Users\\Shruthi\\python-challenge\\Pypoll\\election_data.csv")

# read csv
with open(filepath, newline="",encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # initalize variables
    total_votes = 0
    candidates = []
    candidate_dict = {}
    winner = ""
    winning_votes = 0
    
    # skip header
    next(csvreader)

    # getting total votes and candiate names
    for row in csvreader:
        total_votes += 1
        # if candiate is not in list
        if row[2] not in candidates:
            # add candiate to list
            candidates.append(row[2])
            # keep track of candiate votes
            candidate_dict[row[2]] = 0
        # add vote to candidate
        candidate_dict[row[2]] = candidate_dict[row[2]] + 1

    #printing results

    print("Election Results")
    print("-----------------------------")
    print("Total number of votes: " +str(total_votes))
    print("-----------------------------")

    #to get the percentage of votes and corresponding names
    for candidate in candidate_dict:
        votes = candidate_dict.get(candidate)
        percentage = votes / total_votes
        print(candidate + ':' + str(round(percentage,2)*100) + ' : (' + str(votes) + ')')
        if votes > winning_votes:
            winning_votes = votes
            winner = candidate
    
    #printing winner
    print("-----------------------------")
    print('Winner is: ' + winner + ' (' + str(winning_votes) + ')')

    #getting a text file
    new_file = open("results_1.txt", "w")

# writing the new file
    new_file.write("Election Results \n")
    new_file.write("------------------------------------- \n")
    new_file.write("Total Votes: " +str(total_votes) + "\n")
    new_file.write("------------------------------------- \n")
    for candidate in candidate_dict:
        votes = candidate_dict.get(candidate)
        percentage = votes / total_votes
        new_file.write(candidate + ':' + str(round(percentage,2)*100) + ' : (' + str(votes) + ')''\n')
        if votes > winning_votes:
            winning_votes = votes
            winner = candidate
    new_file.write("------------------------------------- \n")        
    new_file.write('Winner is: ' + winner + ' (' + str(winning_votes) + ')''\n')
    
    #closing of file
    new_file.close()

    