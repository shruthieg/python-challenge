# importing dependencies
import csv
import os
import math

# get csv path
from pathlib import Path
filepath = Path("C:\\Users\Shruthi\\python-challenge\\PyBank\\budget_data.csv")

# read csv
with open(filepath, newline="",encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #initalize variables
    months = []
    revenue = []
    change =[]

    #skip header
    next(csvreader)

    #get total number of months and total revenue
    for row in csvreader:
        months.append(row[0])
        revenue.append(int(row[1]))

    #printing the results for total number of months and total revenue  
    print("---------------------")
    print("FINANCIAL ANALYSIS")
    print("---------------------")
    print("total number of months = "+str(len(months)))
    print("total net amount of profit/losses = " +str(sum(revenue)))

    #difference between months and average difference
    for i in range(1,len(revenue)):
        change.append(revenue[i] - revenue[i-1])
    print("average change =" +str(sum(change)/(len(months)-1)))
    print("greatest increase in profits (date and amount) over the entire period : " +str(months[(change.index(max(change)))+1]) +  ":"  +str(max(change)))
    print("greatest increase in profits (date and amount) over the entire period : " +str(months[(change.index(min(change)))+1]) +  ": ("  +str(min(change))+")") 
    
    #getting a text file
    new_file = open("results.txt", "w")

# writing in the new file
    new_file.write("FINANCIAL ANALYSIS \n")
    new_file.write("------------------------------------- \n")
    new_file.write("total number of months = " +str(len(months)) +"\n")
    new_file.write("total net amount of profit/losses = " +str(sum(revenue)) +"\n")
    for i in range(1,len(revenue)):
        change.append(revenue[i] - revenue[i-1])
    new_file.write("average change =" +str(sum(change)/(len(months)-1)) +"\n")
    new_file.write("greatest increase in profits (date and amount) over the entire period : " +str(months[(change.index(max(change)))+1]) +  ":"  +str(max(change)) +"\n")
    new_file.write("greatest increase in profits (date and amount) over the entire period : " +str(months[(change.index(min(change)))+1]) +  ": ("  +str(min(change))+")" +"\n")
    
    #closing of text file
    new_file.close()
    
    

