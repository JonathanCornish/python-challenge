# import the os module which allows us to create file paths across operating systems
import os
# this is the module for reading csv files
import csv

# Path to collect data from the Resources folder
budget_data_csv = os.path.join('Resources','budget_data.csv')

total_months = 0
net_PL = 0
avg_change_mom = 0
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = 0
greatest_decrease_date = ""

#Read in the csvfile
with open(budget_data_csv, 'r') as csvfile:
    #split the data around commas
    budget_file_reader = csv.reader(csvfile, delimiter=",")

    # read the header row first
    csv_header = next(budget_file_reader)

    #print(f"Header: {csv_header}")

    for row in budget_file_reader:
        # calculate the number of months in the analysis period
        total_months += 1
        #calculate the total Profit/Loss over the entire period
        net_PL += int(row[1])

        # calculate the greatest increase/decrease from month over month
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_date = row[0]


    

print("Total Months: " + str(total_months))
print("Total: " + "$" + str(net_PL))
print("Average Change: " + "$" + str(avg_change_mom))
print("Greatest Increase in Profits: " + greatest_increase_date + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + greatest_decrease_date + " ($" + str(greatest_decrease) + ")")