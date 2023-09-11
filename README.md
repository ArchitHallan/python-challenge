# python-challenge
This is My bootcamp assignment 3, python challenge
 # PyBank

This Python script analyzes the financial data of a company over a period. The data is stored in a CSV file named `budget_data.csv`. The script calculates the total months, total profit/loss, average change, greatest increase in profits, and greatest decrease in profits. The results are printed to the terminal and written to a text file named `financial_analysis.txt`.

### Step-by-Step Explanation

The script begins by importing the necessary modules.

```python
# add dependencies
import os
import csv
```

Next, the script creates a path to the CSV file.

```python
# create path to csv file
csvpath = os.path.join('Resources', 'budget_data.csv')
```

The script then creates lists to store the data from the CSV file.

```python
# create lists to store data
months = []
profit_loss = []
monthly_change = []
```

The script then opens the CSV file and reads the data into the lists.

```python
# open csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # loop through rows in csv file
    for row in csvreader:
        # append months and profit_loss lists
        months.append(row[0])
        profit_loss.append(int(row[1]))
```

The script then calculates the monthly change in profits.

```python
# loop through profit_loss list to calculate monthly change
for i in range(len(profit_loss)-1):
    monthly_change.append(profit_loss[i+1]-profit_loss[i])
```

The script then calculates the total months, total profit/loss, and average change.

```python
# calculate total months
total_months = len(months)

# calculate total profit_loss
total_profit_loss = sum(profit_loss)

# calculate average change
average_change = round(sum(monthly_change)/len(monthly_change), 2)
```

The script then calculates the greatest increase and decrease in profits.

```python
# calculate greatest increase in profits
greatest_increase = max(monthly_change)

# calculate greatest decrease in profits
greatest_decrease = min(monthly_change)
```
The script then calculates the greatest increase/decrease in profits (date and amount) over the entire period.

```python
# find index of greatest increase and decrease

greatest_increase_index = monthly_change.index(greatest_increase)

greatest_decrease_index = monthly_change.index(greatest_decrease)

# find corresponding month of greatest increase and decrease

greatest_increase_month = months[greatest_increase_index+1]

greatest_decrease_month = months[greatest_decrease_index+1]
```
Finally, we print out our results
```python
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")
```
Create path to output file, open and write to analysis text
```python
output_file = os.path.join('Analysis', 'financial_analysis.txt')
with open(output_file, 'w') as textfile:
    xtextfile.write("Financial Analysis\n")
    textfile.write("----------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${total_profit_loss}\n")
    textfile.write(f"Average Change: ${average_change}\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    textfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")
```
 # PyPoll
This Python script analyses the votes that were cast in a tiny small town. The information is saved in a CSV file called 'election_data.csv'. The script computes the total number of votes cast, the complete list of candidates who received votes, the percentage of votes each candidate received, the total number of votes each candidate received, and the election winner based on popular vote. The output is printed to the terminal and saved to the text file 'election_analysis.txt'.

### Step-by-Step Explanation
The script begins by importing the necessary modules.

```python
# add dependencies
import os
import csv
```
Next, the script creates a path to the CSV file.

```python
# create path to csv file
csvpath = os.path.join('Resources', 'election_data.csv')
```
The script then creates lists to store the data from the CSV file.

```python
# create lists to store data
voter_id = []
county = []
candidate = []
```
Then it opens up the CSV using `open()` function with `read` mode. The code loops through each row of the CSV file and appends

```python
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # loop through rows in csv file

    for row in csvreader:
        # append lists
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
```
The script then calculates total votes and creates list of unique candidates
```python
total_votes = len(voter_id)
unique_candidates = list(set(candidate))
```
The script then creates list to store vote count and percent of votes for each candidate. Loop through unique candidates to count votes and loop through vote count list to calculate percent of votes.
```python
vote_count = []
for i in range(len(unique_candidates)):
    vote_count.append(candidate.count(unique_candidates[i]))
percent_votes = []
for i in range(len(vote_count)):
    percent_votes.append(round(vote_count[i]/total_votes*100, 3))
```
Then the scripT finds index of candidate with most votes and find name of candidate with most votes
```python
winner_index = vote_count.index(max(vote_count))
winner = unique_candidates[winner_index]
```
Finally it prints out results on terminal screen using f-strings
```python
print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------')
for i in range(len(unique_candidates)):
    print(f'{unique_candidates[i]}: {percent_votes[i]}% ({vote_count[i]})')
print('-------------------------')
print(f'Winner: {winner}')
print('-------------------------')
```
Create path to output file, open and write to analysis text
```python
output_path = os.path.join('Analysis', 'election_results.txt')

with open(output_path, 'w') as txtfile:
    txtfile.write('Election Results\n')
    txtfile.write('-------------------------\n')
    txtfile.write(f'Total Votes: {total_votes}\n')
    txtfile.write('-------------------------\n')
    for i in range(len(unique_candidates)):
        txtfile.write(f'{unique_candidates[i]}: {percent_votes[i]}% ({vote_count[i]})\n')
    txtfile.write('-------------------------\n')
    txtfile.write(f'Winner: {winner}\n')
    txtfile.write('-------------------------\n')

#---------------------------------------------
```

