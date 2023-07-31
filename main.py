import overheads, cash_on_hand, profit_loss

def main():
    """
    - Function runs overhead_function(), cash_on_hand() and profit_loss() imported respectively from
    overheads.py, cash_on_hand.py and profit_loss.py.
    - Function will produce a "summary_report.txt" text file with all the results from the 3 functions written in it.
    - No required parameters.
    """
    overheads.overhead_function()
    cash_on_hand.cash_on_hand()
    profit_loss.profit_loss()
    
main()
