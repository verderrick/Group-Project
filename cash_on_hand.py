from pathlib import Path
import csv

# create a file to csv file.
fp = Path.cwd()/"CSV Reports"/"cash on hand.csv"

# read the csv file to append the day and cash on hand from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty lists to store the day and cash on hand
    COH = [] 

    # append the day and cash on hand into the COH list
    for row in reader:
        # get the day and cash on hand and append to COH list
        COH.append([row[0],int(row[1])])

def cash_on_hand():
    cash_deficit = []
    prev_day_COH = int(COH[0][1])  

    for current_day in COH[1:]:
        current_day_COH = int(current_day[1])

        if current_day_COH < prev_day_COH:
            difference = prev_day_COH - current_day_COH
            cash_deficit.append((current_day[0], difference))

        prev_day_COH = current_day_COH  

    from overheads import overhead_function
    with open("summary_report.txt", mode = "a", encoding = "UTF-8") as file:
        for item in cash_deficit:
            file.write(f"[CASH DEFICIT] DAY: {item[0]}, AMOUNT: USD{item[1]}\n")
