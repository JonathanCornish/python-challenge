import os
import csv

# Path to collect data from the Resources folder
budget_data_csv = os.path.join('..','Resources','budget_data.csv')

total_months = 0
net_PL = 0
avg_change_mom = 0
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = 0
greatest_decrease_date = ""

print("Total Months: " + str(total_months))
print("Total: " + str(net_PL))
print("Average Change: " + str(avg_change_mom))
print("Greatest Increase in Profits: " + greatest_decrease_date + "($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + greatest_increase_date + "($" + str(greatest_decrease) + ")")