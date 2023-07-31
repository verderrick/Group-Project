from pathlib import Path
import csv

# create a file to csv file.
fp = Path.cwd()/"CSV Reports"/"profit & loss.csv"

# read the csv file to append the day and net profit from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty lists to store the day and net profit
    PL = [] 

    # get the day and net profit and append to PL list
    for row in reader:
        # append the day and net profit into the PL list
        PL.append([row[0],int(row[5])])

from overheads import overhead_function

def profit_loss():
    """
    - Function will compute the difference in the net profit column 
    if net profit on the current day is lower than the previous day.
    - If the net profit is always increasing, the function will find out
    the day and amount the highest increment occurs.
    - Function will write the results to the "summary_report.txt" text file
    imported from overhead_function in overheads.py file.
    - No required parameters.
    """

    # create an empty list to store the profit deficits
    profit_deficit = []

    # initialize the previous day's net profit to the first day's net profit
    prev_day_prof = int(PL[0][1])  

    # initialize the highest increment to 0
    highest_increment = 0

    # set a variable to True to track if net profit is always increasing or not
    always_increasing = True

    # loop through the PL list starting from the first day
    for current_day in PL[1:]:
        # extract the net profit value for the current day
        current_day_prof = int(current_day[1])

        if current_day_prof < prev_day_prof:
             # set variable to false since net profit is not always increasing
            always_increasing = False
            # calculate the net profit deficit
            difference = prev_day_prof - current_day_prof
            # append the net profit deficit amount and its respective day to the profit deficit list
            profit_deficit.append((current_day[0], difference))

        elif always_increasing == True and current_day_prof > prev_day_prof: 
            # calculate the increment in net profit
            increment = current_day_prof - prev_day_prof
            # check if this increment is the highest 
            if increment > highest_increment:
                # update the new amount for the highest increment
                highest_increment = increment

         # update the previous day's net profit for the next loop
        prev_day_prof = current_day_prof

    # write the results to the text file imported from overheads.py
    with open("summary_report.txt", mode = "a", encoding = "UTF-8") as file:

        # write each net profit deficit to the file
        for item in profit_deficit:
            file.write(f"[PROFIT DEFICIT] DAY: {item[0]}, AMOUNT: USD{item[1]}\n")

        # if net profit is always increasing, write the results to the file
        if always_increasing == True:
            file.write(f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")
            file.write(f"[HIGHEST NET PROFIT SURPLUS] DAY: {current_day[0]}, AMOUNT: USD{highest_increment}\n")