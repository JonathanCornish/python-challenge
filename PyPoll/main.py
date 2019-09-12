# import the os module which allows us to create file paths across operating systems
import os
# this is the module for reading csv files
import csv

# Path to collect data from the Resources folder
election_data_csv = os.path.join('Resources','election_data.csv')

total_votes = 0
most_votes = 0
election_winner = ""
candidate_list = []
count_candidate_votes = {}

#Read in the csvfile
with open(election_data_csv, 'r') as csvfile:
    #split the data around commas
    election_file_reader = csv.reader(csvfile, delimiter=",")

    # read the header row first
    csv_header = next(election_file_reader)

    # the following line was a test to check that the program was working okay:
    # print(f"Header: {csv_header}")
    # print(f"Total Votes: {total_votes}")

    for row in election_file_reader:
        # calculate the number of votes in the analysis period
        total_votes += 1
        
        # add candidate to candidate_list if they are not already in the candidate_list
        if not row[2] in candidate_list:
            candidate_list.append(row[2])
            count_candidate_votes[row[2]] = 0
        # calculate total no. of votes each candidate won:
        count_candidate_votes[row[2]] +=1    
        
        
    # for candidate in candidate_list:
    #     print(count_candidate_votes)
    # print(count_candidate_votes)
    # print(count_candidate_votes['Khan'])
    print(f"Election Results:")
    print(f"-------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"-------------------------")

    for candidate, value in count_candidate_votes.items():
        if value > most_votes:
            most_votes = value
            election_winner = candidate
        
        print(f"{candidate}: {format(value/total_votes*100, '.3f')}% ({value})")
    print(f"-------------------------")
    print(f"Winner: {election_winner}")
    print(f"-------------------------")









# create the file to write to
election_data_txt_output = os.path.join('budget_data_txt.txt')

# Open the file using "write" mode. Specify the variable to hold the contents
with open(election_data_txt_output, 'w', newline='') as txtfile:


    # simply print everything you want into the text file
    txtfile.write("Election Results: " + "\n")
    txtfile.write("-----------------------------" + "\n")
    txtfile.write("Total Votes: " + str(total_votes) + "\n")
    txtfile.write("-----------------------------" + "\n")
    txtfile.write("WHERE THE INDIVIDUAL CANDIDATES' STUFF WILL GO" + "\n")
    txtfile.write("-----------------------------" + "\n")
    txtfile.write("Winner: " + election_winner + "\n")
    txtfile.write("-----------------------------" + "\n")

