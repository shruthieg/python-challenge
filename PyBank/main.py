#main code here
import csv
import os
import math

from pathlib import Path
filepath = Path("C:\\Users\Shruthi\\python-challenge\\PyBank\\budget_data.csv")
with open(filepath, newline="",encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    months = []
    revenue = []
    change =[]
    next(csvreader)
    for row in csvreader:
        months.append(row[0])
        revenue.append(int(row[1]))
    print("FINANCIAL ANALYSIS")
    print("total number of months = "+str(len(months)))
    print("total net amount of profit/losses = " +str(sum(revenue)))
    for i in range(1,len(revenue)):
        change.append(revenue[i] - revenue[i-1])
    print("change between months = "+str(change))
    print("average change =" +str(sum(change)/(len(months)-1)))
    #print(max(change))
    #print(months[(change.index(max(change)))+1])
    print("greatest increase in profits (date and amount) over the entire period : " +str(months[(change.index(max(change)))+1]) +  ":"  +str(max(change)))
    #print(min(change))  
    #print(months[(change.index(min(change)))+1])
    print("greatest increase in profits (date and amount) over the entire period : " +str(months[(change.index(min(change)))+1]) +  ": ("  +str(min(change))+")") 
#output = out_fun():
    #file = open("output.txt","w")
    #file.write(output)
    #file.close()

