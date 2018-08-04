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
    #name_percent= {}
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
        # add vote to candiadate
        candidate_dict[row[2]] = candidate_dict[row[2]] + 1

    print(candidates)
    print(candidate_dict)

    print("Vote Results")
    print("-----------------------------")
    print("Total number of votes: " +str(total_votes))
    print("-----------------------------")
    for candidate in candidate_dict:
        votes = candidate_dict.get(candidate)
        percentage = votes / total_votes
        print(candidate + ' ' + str(round(percentage,3)*100) + ': (' + str(votes) + ')')
        if votes > winning_votes:
            winning_votes = votes
            winner = candidate

    print('Winner: ' + winner + ' (' + str(winning_votes) + ')')
# #to get the percent of votes of each candidate
#     for i in candidates: 
#         #(candidates[i]/votes)*100
#         percent.append(round((candidates[i]/votes)*100,3))
#     print(percent)
#     print("Winner is :" +str(max(percent)))
#     maximum = max(candidates, key = candidates.get)
#     print(maximum,candidates[maximum])
#     for key, value, in candidates.items():
#         print(key + ": "  + " (" + str(value) + ")")
    
    #text_file = open("write_it.txt", "w")
    #lines = ["Line 1\n",
       #"This is line 2\n",
       #"That makes this line 3\n"]
    #text_file.writelines(lines)
    #text_file.close()
    
    



#newfile = open("output\results.txt, "w")
    


    
