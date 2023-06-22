# Import Modules
import os
import csv

# Declare the list and variables
candidates = []
final_list = []
total_votes_each_candidate = 0

# Set path for reading the file
csvpath = os.path.join("Resources", "election_data.csv")

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip the header
    csv_header = next(csvreader)
    for row in csvreader:
        candidates.append(row[2])

total_votes = len(candidates)
candidates = sorted(candidates)
# Loop through the candidates list to get final list of all the different candidates and the total votals for each candidate
for i in range(len(candidates)-1):
    if candidates[i+1] != candidates[i]:
        total_votes_each_candidate = total_votes_each_candidate + 1
        final_list.append([candidates[i],total_votes_each_candidate])
        total_votes_each_candidate = 0
    else:
        total_votes_each_candidate = total_votes_each_candidate + 1

# Add the final candidate data to the list
total_votes_each_candidate = total_votes_each_candidate + 1
final_list.append([candidates[i],total_votes_each_candidate])

# Set path for writing the file
csvpath = os.path.join("analysis", "election_data.txt")
# Write the file with required output information
with open(csvpath,'w') as csvfile:
    csvfile.write('Election Results\n\n')
    csvfile.write('-------------------------\n\n')
    csvfile.write(f'Total Votes: {total_votes}\n\n')
    csvfile.write('-------------------------\n\n')
    winner_count = int(final_list[0][1])
    winner = final_list[0][0]
    for i in range(len(final_list)):
        csvfile.write(f'{final_list[i][0]} {round((int(final_list[i][1])/total_votes)*100,3)}% ({int(final_list[i][1])})\n\n')
        if int(final_list[i][1]) > winner_count:
            winner = final_list[i][0]
    csvfile.write('-------------------------\n\n')
    csvfile.write(f'Winner: {winner}\n\n')
    csvfile.write('-------------------------\n\n')

# Print the output information to terminal
print('Election Results\n')
print('-------------------------\n')
print(f'Total Votes: {total_votes}\n')
print('-------------------------\n')
for i in range(len(final_list)):
    print(f'{final_list[i][0]} {round((int(final_list[i][1])/total_votes)*100,3)}% ({int(final_list[i][1])})\n')
print('-------------------------\n')
print(f'Winner: {winner}\n')
print('-------------------------\n')
