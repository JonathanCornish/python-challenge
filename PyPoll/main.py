print(f'Hello World')

# import the os module which allows us to create file paths across operating systems
import os
# this is the module for reading csv files
import csv

# Path to collect data from the Resources folder
election_data_csv = os.path.join('Resources','election_data.csv')

total_votes = 0
election_winner = ""

#Read in the csvfile
with open(election_data_csv, 'r') as csvfile:
    #split the data around commas
    election_file_reader = csv.reader(csvfile, delimiter=",")

    # read the header row first
    csv_header = next(election_file_reader)

    # the following line was a test to check that the program was working okay:
    print(f"Header: {csv_header}")
    print(f"Total Votes: {total_votes}")

#     # method to get the previous file row:
#     pre_row = next(election_file_reader)
    
#     #print(f"preline: {pre_row}")
    
#     # # method below as alternative to calculate the mom change
#     # PL_change = 0
#     # previous_PL = 0
    
    
    for row in election_file_reader:
        # calculate the number of votes in the analysis period
        total_votes += 1
print(f"Total Votes: {total_votes}")
#         # calculate the total Profit/Loss over the entire period
#         net_PL += int(row[1])

#         # calculate the total change from month-over-month:
#         tot_change_mom += int(row[1]) - int(pre_row[1])

#         # calculate the greatest increase/decrease from month over month
#         if (int(row[1]) - int(pre_row[1])) > greatest_increase:
#             greatest_increase = int(row[1]) - int(pre_row[1])
#             greatest_increase_date = row[0]
        
#         elif (int(row[1]) - int(pre_row[1])) < greatest_decrease:
#             greatest_decrease = int(row[1]) - int(pre_row[1])
#             greatest_decrease_date = row[0]
#         pre_row = row

#         # or, using previous_PL method...
#         # PL_change = row[1] - previous_PL
#         # previousl_PL = row[1]

# avg_change_mom = tot_change_mom / total_votes
# avg_change_mom = round(avg_change_mom, 2)
    

# print("Total votes: " + str(total_votes))
# print("Total: " + "$" + str(net_PL))
# print("Average Change: " + "$" + str(avg_change_mom))
# print("Greatest Increase in Profits: " + greatest_increase_date + " ($" + str(greatest_increase) + ")")
# print("Greatest Decrease in Profits: " + greatest_decrease_date + " ($" + str(greatest_decrease) + ")")

# # # the below line is only relevant for method (1) of printing to the txt file:
# # summary_results = list(zip([total_votes, net_PL, avg_change_mom, greatest_increase, greatest_increase_date, greatest_decrease, greatest_decrease_date]))
# # create the file to write to
# election_data_txt_output = os.path.join('election_data_txt.txt')

# # Open the file using "write" mode. Specify the variable to hold the contents
# with open(election_data_txt_output, 'w', newline='') as txtfile:

#     # # Two ways to put this into the text file:
#     # # (1) Initialize txt.writer
#     # txtwriter = csv.writer(txtfile, delimiter=',')
#     # txtwriter.writerow(["Total votes", "Total", "Average Change", "Greatest Increase in Profits", "Greatest Increase Date",
#     # "Greatest Decrease in Profits", "Greatest Decrease"])
#     # txtwriter.writerow(summary_results)

#     # # (2) simply print everything you want into the text file
#     txtfile.write("Total votes: " + str(total_votes) + "\n")
#     txtfile.write("Total: " + "$" + str(net_PL) + "\n")
#     txtfile.write("Average Change: " + "$" + str(avg_change_mom) + "\n")
#     txtfile.write("Greatest Increase in Profits: " + greatest_increase_date + " ($" + str(greatest_increase) + ")" + "\n")
#     txtfile.write("Greatest Decrease in Profits: " + greatest_decrease_date + " ($" + str(greatest_decrease) + ")" + "\n")

