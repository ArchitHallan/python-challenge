#PyPoll Solution

# import modules
import os
import csv

# create path to csv file

csvpath = os.path.join('Resources', 'election_data.csv')

# create lists to store data

voter_id = []
county = []
candidate = []

# open csv file

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # loop through rows in csv file

    for row in csvreader:
        # append lists
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

# calculate total votes

total_votes = len(voter_id)

# create list of unique candidates

unique_candidates = list(set(candidate))

# create list to store vote count for each candidate

vote_count = []

# loop through unique candidates to count votes

for i in range(len(unique_candidates)):
    vote_count.append(candidate.count(unique_candidates[i]))

# create list to store percent of votes for each candidate

percent_votes = []

# loop through vote count list to calculate percent of votes

for i in range(len(vote_count)):
    percent_votes.append(round(vote_count[i]/total_votes*100, 3))

# find index of candidate with most votes

winner_index = vote_count.index(max(vote_count))

# find name of candidate with most votes

winner = unique_candidates[winner_index]

# print analysis to terminal

print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------')
for i in range(len(unique_candidates)):
    print(f'{unique_candidates[i]}: {percent_votes[i]}% ({vote_count[i]})')
print('-------------------------')
print(f'Winner: {winner}')
print('-------------------------')

# export analysis to text file

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




