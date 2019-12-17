import os
import csv

# Path to open PyBank data
budget_data_csv = os.path.join('PyBank_Resources_budget_data.csv')
 

# Read in the CSV file
with open(budget_data_csv, 'r') as csvfile:
    month_to_check = []
    revenue = []
    row = []
    change_earnings = []
    averange_change = 0
    Total = 0
    greatest_increase = 0
    greatest_increase_month = []
    greatest_decrease = 0
    greatest_decrease_month = []
   
    csvreader = csv.reader(csvfile, delimiter=',')
    
    header = next(csvreader)
   
    # Loop through the data
    for row in csvreader:
        revenue.append(int(row[1]))
        month_to_check.append(row[0])
        Total = Total + int(row[1])
       
    for i in range(len(revenue)-1):
        change_earnings.append(revenue[i+1]-revenue[i])    
        # Calculate greatest increase
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
        # Calculate greatest decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
        # Calculate average change
        average_change = sum(change_earnings)/len(change_earnings)
    greatest_increase = max(change_earnings)
    greatest_decrease = min(change_earnings)
     
    # Look for the maximum and minimm revenue
    max_revenue = max(revenue)

    min_revenue = min(revenue)
    
    greatest_increase_month = month_to_check[revenue.index(max_revenue)]
    greatest_decrease_month = month_to_check[revenue.index(min_revenue)]
    # print out results
    print("Financial Analysis")
    print(("------------------------"))
    print("Total Months: " + str(len(month_to_check)))
    print("Total: $", str(Total)) 
    print(f"Average Change: ${average_change:0.2f}")
    print("Greatest Increase in Profits: " + str(greatest_increase_month) + " ($ " + str(greatest_increase) + ")")
    print("Greatest Decrease in Profits: " + str(greatest_decrease_month)+ "  ($ " + str(greatest_decrease) + ")")

output = os.path.join(".", 'Final_Stats_Analysis.txt')
with open(output,"w") as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("------------------------\n")
    textfile.write(f"Total Months:{len(month_to_check)}\n")
    textfile.write(f"Total: ${Total}\n")
    textfile.write(f"Average Change: ${average_change:0.2f}\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${(str(greatest_increase))})\n")
    textfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${(str(greatest_decrease))})")