from pathlib import Path
import csv

# create a file to csv file.
fp = Path.cwd()/"CSV Reports"/"overheads.csv"

# read the csv file to append profit and quantity from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty lists to store time sheet and sales record
    overheads = [] 

    # append time sheet and sales record into the salesRecords list
    for row in reader:
        #get the employee id, toal hours, break hours, and sales for each record
        #and append the salesRecords list
        overheads.append([row[0],float(row[1])])   

higest_overheads = []
for item in overheads:
    higest_overheads.append(item[1])

def overhead_function():

    with open('summary.txt', 'w') as file:
        for item in overheads:
            if item[1] == max(higest_overheads):
                file.write(f"[HIGHEST OVERHEAD] {item[0].upper()}: {item[1]}%")