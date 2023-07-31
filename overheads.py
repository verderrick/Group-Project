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

    # get the category and overheads and append to the overheads list 
    for row in reader: 
        # append category and overheads into the overheads list 
        overheads.append([row[0],float(row[1])])   


def overhead_function():
    """
    - Function will find the highest overhead category.
    - Function will create a text file called "summary_report.txt"
    - The computed category and overhead amount will be written to the "summary_report.txt" file.
    - No required parameters.
    """

    # create an empty list to store all the overhead amounts
    higest_overheads = []
    for item in overheads:
        # append the overhead amounts into the list
        higest_overheads.append(item[1])

    # write the results to a text file
    with open('summary_report.txt', 'w') as file:
        for item in overheads:
            # find the highest overhead amount 
            if item[1] == max(higest_overheads):
                # write the respective category and its overhead amount to the text file
                file.write(f"[HIGHEST OVERHEAD] {item[0].upper()}: {item[1]}%\n")