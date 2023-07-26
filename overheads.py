from pathlib import Path
import csv

# create a file to csv file.
fp = Path.cwd()/"CSV Reports"/"overheads.csv"

# read the csv file to append category and overheads from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty lists to store the category and overheads
    overheads = [] 

    # append category and overheads into the overheads list
    for row in reader:
        # get the category and overheads and append to the overheads list   
        overheads.append([row[0],float(row[1])])   



def overhead_function():
    higest_overheads = []
    for item in overheads:
        higest_overheads.append(item[1])

    with open('summary_report.txt', 'w') as file:
        for item in overheads:
            if item[1] == max(higest_overheads):
                file.write(f"[HIGHEST OVERHEAD] {item[0].upper()}: {item[1]}%")