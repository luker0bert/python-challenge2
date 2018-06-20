# Your task is to create a Python script that analyzes the records to calculate each of the following:

# As an example, your analysis should look similar to the one below:

#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import os
import csv

# Path to obtain CSV data
budget_dataCSV = os.path.join('..', "PyBank", "budget_data.csv")

# Read in the csv file
with open(budget_dataCSV, 'r') as csvfile:

    # # split data on the commas
    csvreader = csv.reader(csvfile)

    # Pass over header
    csv_header = next(csvreader)

    # initialize variable to zero
    total_months = 0
    net_revenue = 0
    greatest_Increase_Revenue = []
    greatest_Decrease_Revenue = []
    date = []

    # Loop through data
    for row in csvreader:
        # The total number of months included in the dataset
        total_months += 1
        net_revenue += float(row[1])
        # for i in range(1,len(net_revenue)):
        #     greatest_Increase_Revenue.append(net_revenue[i] - net_revenue(i -1))
        #     avg_net_revenue = sum(net_revenue/len(net_revenue))
        #     greatest_increase_Revenue = max(net_revenue)
        #     greatest_Decrease_Revenue = min(net_revenue)
        for row in range(1, net_revenue):
            if net_revenue(row[i] - net_revenue[i - 1]) > net_revenue(row[1])
                print greatest_Increase_Revenue
            else:
                pass
        
    #Print out data
    print("FINANCIAL ANALYSIS")
    print("___________________")
    print(f"Total Months: {str(total_months)}")
    print(f"Total Revenue: $ {str(net_revenue)}")
    # print(f"Greatest Increase in Profits: " ++ greatest_Increase_Revenue)
    # print(f"Greatest Decrease in Profits: " ++ greatest_Decrrease_Revenue)