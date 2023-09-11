# add dependencies
import os
import csv

# create path to csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

# create lists to store data
months = []
profit_loss = []
monthly_change = []

# open csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # loop through rows in csv file
    for row in csvreader:
        # append months and profit_loss lists
        months.append(row[0])
        profit_loss.append(int(row[1]))

    # loop through profit_loss list to calculate monthly change
    for i in range(len(profit_loss)-1):
        monthly_change.append(profit_loss[i+1]-profit_loss[i])

# calculate total months
total_months = len(months)

# calculate total profit_loss

total_profit_loss = sum(profit_loss)

# calculate average change

average_change = round(sum(monthly_change)/len(monthly_change), 2)

# calculate greatest increase in profits

greatest_increase = max(monthly_change)

# calculate greatest decrease in profits

greatest_decrease = min(monthly_change)

# find index of greatest increase and decrease

greatest_increase_index = monthly_change.index(greatest_increase)

greatest_decrease_index = monthly_change.index(greatest_decrease)

# find corresponding month of greatest increase and decrease

greatest_increase_month = months[greatest_increase_index+1]

greatest_decrease_month = months[greatest_decrease_index+1]

# print analysis to terminal

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# create path to output file
output_file = os.path.join('Analysis', 'financial_analysis.txt')

# open output file
with open(output_file, 'w') as textfile:
    # write analysis to text file
    textfile.write("Financial Analysis\n")
    textfile.write("----------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${total_profit_loss}\n")
    textfile.write(f"Average Change: ${average_change}\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    textfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")



