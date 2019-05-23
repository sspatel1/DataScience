##############################################################################################
#  
# Analyze the financial records of a company from a  fiven financial data called budget_data.csv.
# The dataset is composed of two columns: Date and Profit/Losses.
#
# Analyzes the records to calculate each of the following:
# (a) The total number of months included in the dataset
# (b) The net total amount of "Profit/Losses" over the entire period
# (c) The average of the changes in "Profit/Losses" over the entire period
# (d) The greatest increase in profits (date and amount) over the entire period
#  (e) The greatest decrease in losses (date and amount) over the entire period
# 
#################################################################################################

# Modules
import os
import csv
from sys import exit


# Set path for file
filename = "budget_data.csv"
csvpath = os.path.join("..", "Resources", filename)

# Print absolute path for this file. Just for reference
print(os.path.abspath(__file__))


# --------------------------------------------------------------------------
# Use "try"-"except" to prevent program crash due to file not available 
# --------------------------------------------------------------------------
try:
    with open(csvpath, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        next(csvreader) # skip the Header

        # csvreader reads csv file rows as a a list. 
        # It is difficult to work with seperate lists (one row at a time).
        #  
        # We will create a new list called "profilt_loss_list[]" which will store
        # each row as list (one list per row) in to this list.
        # This means we will create a list of lists!!!
        #
        # For example the new list will look like (for illustration purpose):
        # profilt_loss_list = [ [Row1], [Row2], [Row3], etc....]

        # Creat a new list
        profit_loss_list = list()

        # Read each row using csvreader and append to list profit_loss_list[].
        for row in csvreader:
            # Append each row from csvreader
            profit_loss_list.append(row)
   
except FileNotFoundError:
        # Handle missing file with exception.
        # Print out clear message to the user.
        # Make a clean exit.
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
        exit()


# Sum each months profit (loss) over entire period
total_profit_loss = 0
for row in profit_loss_list:
    total_profit_loss = total_profit_loss + int(row[1])
    


# Numer of months
length = len(profit_loss_list)

# Initialization of variables
sum_of_profit_loss_change = 0
greatest_increase_in_profit = 0
greatest_decrease_in_profit = 0

# Find month over month difference in profit (loss) amount over entire period.
# Find the greatest month over month increase (profit) and 
# greatest month over month decrease (loss)
for i in range(length-1):
    profit_loss_change = int(profit_loss_list[i+1][1]) - int(profit_loss_list[i][1])

    if profit_loss_change >= greatest_increase_in_profit:
        greatest_increase_in_profit = profit_loss_change
        greatest_increase_month = profit_loss_list[i+1][0]

    if profit_loss_change < greatest_decrease_in_profit:
        greatest_decrease_in_profit = profit_loss_change
        greatest_decrease_month = profit_loss_list[i+1][0]

    sum_of_profit_loss_change = sum_of_profit_loss_change + profit_loss_change


# caluclate the average chagne in profit (loss) over entire period         
average_change = sum_of_profit_loss_change/(length-1)

msg1 = 'Financial Analysis'
msg2 = '-------------------------'
msg3 = f'Total Months: {length}'
msg4 = f'Total: ${total_profit_loss}'
msg5 = 'Average Change: ${0:.2f}'.format(average_change)
msg6 = f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_in_profit})'
msg7 = f'Greatest Decrease in Profits: {greatest_increase_month} (${greatest_decrease_in_profit})'

print(msg1)
print(msg2)
print(msg3)
print(msg4)
print(msg5)
print(msg6)
print(msg7)



# Set path for result file
filename = "PyBank.txt"

# Write the result to the file
with open(filename, 'w') as txtwrite:
    txtwrite.write(msg1+'\n')
    txtwrite.write(msg2+'\n')
    txtwrite.write(msg3+'\n')
    txtwrite.write(msg4+'\n')
    txtwrite.write(msg5+'\n')
    txtwrite.write(msg6+'\n')
    txtwrite.write(msg7+'\n')
