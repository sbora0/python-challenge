# Import Modules
import os
import csv

# Declare the list and variables
months = []
amounts = []
total_months = 0
total = 0
average_change = 0
greatest_inc_profit = 0
greatest_dec_profit = 0

# Set path for reading the file
csvpath = os.path.join("Resources", "budget_data.csv")

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip the header
    csv_header = next(csvreader)
    # Add data to new lists
    for row in csvreader:
        months.append(row[0])
        amounts.append(row[1])

# Count the total number of records in list
total_months = len(months)
# Loop over the list to get the total
for row in amounts:
    total = total + int(row)
# Loop over the list to get the average change
for i in range(len(amounts)-1):
    average_change = average_change + (int(amounts[i+1]) - int(amounts[i]))
# Loop over the list to get the greatest increase in profit
for i in range(len(amounts)-1):
    if (int(amounts[i+1]) - int(amounts[i])) > greatest_inc_profit:
        greatest_inc_profit = int(amounts[i+1]) - int(amounts[i])
        greatest_inc_profit_month = months[i+1]
# Loop over the list to get the greatest decrease in profit
for i in range(len(amounts)-1):
    if (int(amounts[i+1]) - int(amounts[i])) < greatest_dec_profit:
        greatest_dec_profit = int(amounts[i+1]) - int(amounts[i])
        greatest_dec_profit_month = months[i+1]

# Set path for writing the file
csvpath = os.path.join("analysis", "budget_data.txt")
# Write the file with required output information
with open(csvpath,'w') as csvfile:
    csvfile.write('Financial Analysis\n\n')
    csvfile.write('-------------------------------\n\n')
    csvfile.write(f'Total Months: {total_months}\n\n')
    csvfile.write(f'Total: ${total}\n\n')
    csvfile.write(f'Average Change: ${round(average_change/(len(amounts)-1),2)}\n\n')
    csvfile.write(f'Greatest Increase in Profits: {greatest_inc_profit_month} (${greatest_inc_profit})\n\n')
    csvfile.write(f'Greatest Decrease in Profits: {greatest_dec_profit_month} (${greatest_dec_profit})\n\n')
    

# Print the output information to terminal
print('Financial Analysis\n')
print('-------------------------------\n')
print(f'Total Months: {total_months}\n')
print(f'Total: ${total}\n')
print(f'Average Change: ${round(average_change/(len(amounts)-1),2)}\n')
print(f'Greatest Increase in Profits: {greatest_inc_profit_month} (${greatest_inc_profit})\n')
print(f'Greatest Decrease in Profits: {greatest_dec_profit_month} (${greatest_dec_profit})\n')