import csv
import random

random.seed()
table = []
for r in range(5):
    row = []
    for c in range(5):
        thisNumber = round(random.random(), 2)
        row.append(thisNumber)
    table.append(row)
print(table)

with open("myTable.csv", "w+", encoding="utf-8", newline="") as myCSV:
    csvWriter = csv.writer(myCSV)
    csvWriter.writerows(table)
