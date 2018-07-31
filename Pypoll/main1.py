import csv
import os
import math 

from pathlib import Path
filepath = Path("C:\\Users\\Shruthi\\python-challenge\\Pypoll\\election_data.csv")
with open(filepath, newline="",encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    votes = 0
    candidates = {}
    next(csvreader)
    for row in csvreader:
        votes += 1
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1
    print(votes)
    print(candidates)

    
