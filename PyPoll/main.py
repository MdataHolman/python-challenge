# Importing modules important for the analysis
import os
import csv

#To set the path for csv file
election_data = os.path.join('.', 'Resources', 'election_data.csv')

# To set names of candidates
candidates_name = []

# To set number of votes each candidate receives
number_votes = []

# To set the percentage of total votes each candidates
percent_votes = []

# To set the total number of votes
total_votes = 0

# To open and read the csv file
with open(election_data, newline="") as electionfile:
    csvreader = csv.reader(electionfile, delimiter=",")
    csv_header = next(csvreader)

    #To loop through the row
    for row in csvreader:
        # To add vote-counter
        total_votes += 1
        #print(total_votes) - tested the count here 

        # To count the votes per candidate name per row
        if row[2] not in candidates_name:
            candidates_name.append(row[2])
            index = candidates_name.index(row[2])
            number_votes.append(1)
        else:
            index = candidates_name.index(row[2])
            number_votes[index] += 1
    # To get percent_votes list
    for votes in number_votes:
        percentage = (votes/total_votes) * 100
        percentage = "%0.3f%%" % percentage
        percent_votes.append(percentage)
        #print(percent_votes)

    # To get the greatest number of votes(winner) and candidate name
    winner = max(number_votes)
        #print(winner)
    index = number_votes.index(winner)
        #print(index)
    winning_candidate = candidates_name[index]
        #print(winning_candidate)

# To print the output
print("Election Results")
print('\n')
print("--------------------------")
print('\n')
print(f"Total Votes: {str(total_votes)}")
print('\n')
print("--------------------------")
print('\n')
for c in range(len(candidates_name)):
    print(f"{candidates_name[c]}: {str(percent_votes[c])} ({str(number_votes[c])})")
    print('\n')
print("--------------------------")
print('\n')
print(f"Winner: {winning_candidate}" + "!")
print('\n')
print("--------------------------")




# To export to text file to analysis folder

output_file = os.path.join('.', 'analysis', 'pyPoll_output.txt')

pyPoll_output = open(output_file, "w")

line1 = "Election Results"
line2 = "--------------------------"
line3 = " "
line4 = str(f"Total Votes: {str(total_votes)}")
line5 = " "
line6 = str("--------------------------")
line7 = " "
pyPoll_output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4, line5, line6, line7))
for c in range(len(candidates_name)):
    line = str(
        f"{candidates_name[c]}: {str(percent_votes[c])} ({str(number_votes[c])})")
    pyPoll_output.write('{}\n'.format(line))
line8 = "--------------------------"
line9 = " "
line10 = str(f"Winner: {winning_candidate}" + "!")
line11 = " "
line12 = "--------------------------"
line13 = "end poll"
pyPoll_output.write('{}\n{}\n{}\n{}\n{}\n{}\n'.format(line8, line9, line10, line11, line12, line13))
pyPoll_output.close()