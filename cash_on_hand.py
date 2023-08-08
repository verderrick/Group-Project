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

    # get the day and cash on hand and append to COH list
    for row in reader:
        # append the day and cash on hand into the COH list
        COH.append([row[0],int(row[1])])

from overheads import overhead_function

def cash_on_hand():
    """
    - Function will compute the difference in Cash-on-Hand if the current day is
    lower than the previous day. 
    - If the Cash-on-Hand is always increasing, the function will find out
    the day and amount the highest increment occurs.
    - Function will write the results to the "summary_report.txt" text file
    imported from overhead_function in overheads.py file.
    - No required parameters.
    """

    # create an empty list to store the cash deficits
    cash_deficit = []

    # initialize the previous day's cash on hand to the first day's cash on hand
    prev_day_COH = int(COH[0][1])  

    # initialize the highest increment to 0
    highest_increment = 0

    # set a variable to True to track if cash on hand is always increasing or not
    always_increasing = True

    # loop through the COH list starting from the first day
    for current_day in COH[1:]:
        # extract the cash on hand value for the current day
        current_day_COH = int(current_day[1])

        if current_day_COH < prev_day_COH:
            # set variable to false since cash on hand is not always increasing
            always_increasing = False
            # calculate the cash deficit
            difference = prev_day_COH - current_day_COH
            # append the cash deficit amount and its respective day to the cash deficit list
            cash_deficit.append((current_day[0], difference))
        
        elif always_increasing == True and current_day_COH > prev_day_COH: 
            # calculate the increment in cash on hand
            increment = current_day_COH - prev_day_COH
            # check if this increment is the highest 
            if increment > highest_increment:
                # update the new amount for the highest increment
                highest_increment = increment
        
        # update the previous day's cash on hand for the next loop
        prev_day_COH = current_day_COH  
    
    # write the results to the text file imported from overheads.py
    with open("summary_report.txt", mode = "a", encoding = "UTF-8") as file:
        
        # write each cash deficit to the file
        for item in cash_deficit:
            file.write(f"[CASH DEFICIT] DAY: {item[0]}, AMOUNT: USD{item[1]}\n")
        
        # if cash on hand is always increasing, write the results to the file
        if always_increasing == True:
            file.write(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")
            file.write(f"[HIGHEST CASH SURPLUS] DAY: {current_day[0]}, AMOUNT: USD{highest_increment}\n")
    
hi
