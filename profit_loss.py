from pathlib import Path
import csv

# create a file to csv file.
fp = Path.cwd()/"CSV Reports"/"profit & loss.csv"

# read the csv file to append the day and cash on hand from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty lists to store the day and cash on hand
    PL = [] 

    # append the day and cash on hand into the COH list
    for row in reader:
        # get the day and cash on hand and append to COH list
        PL.append([row[0],int(row[5])])

def profit_loss():
    profit_deficit = []
    prev_day_prof = int(PL[0][1])  

    for current_day in PL[1:]:
        current_day_prof = int(current_day[1])

        if current_day_prof < prev_day_prof:
            difference = prev_day_prof - current_day_prof
            profit_deficit.append((current_day[0], difference))

        prev_day_prof = current_day_prof

    from overheads import overhead_function
    with open("summary_report.txt", mode = "a", encoding = "UTF-8") as file:
        for item in profit_deficit:
            file.write(f"[PROFIT DEFICIT] DAY: {item[0]}, AMOUNT: USD{item[1]}\n")