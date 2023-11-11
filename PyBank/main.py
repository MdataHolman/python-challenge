#PyBank Challenge

import os
import csv

#Get data from resources folder
csvpath = os.path.join(".", "Resources", "budget_data")
with open(csvpath, encoding = "UTF-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
print(csvreader)