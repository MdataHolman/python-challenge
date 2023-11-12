# Importing modules important for the analysis
import os
import csv
# To get path for csv file
data_path=os.path.join('.', 'Resources', 'budget_data.csv')

# To set total number of months
number_of_months = 0

# To set total profit and loss
net_profit_loss = 0

# To set for the output value of net profit and/or loss
net_value = 0

# To set for the change of net profit and/or loss
change_net_profit_loss = 0

# Dates of the financial records
dates = []

# Value of net profits and/or loss
net_profits = []

# Read csv file
with open(data_path, newline="") as budget_file:
    csvreader = csv.reader(budget_file, delimiter=",")
    csv_header = next(csvreader)
    # To read the first row
    first_row = next(csvreader)

    # To read the next row of date
    number_of_months += 1

    # Add profit and loss counter
    net_profit_loss += int(first_row[1])
    net_value = int(first_row[1])

    # Read the rows after the header row
    for row in csvreader:

        # Get the date
        dates.append(row[0])

        # Keep the the records of changes in rows
        change_net_profit_loss = int(row[1])- net_value
        net_profits.append(change_net_profit_loss)
        net_value = int(row[1])

        # Total number of months
        number_of_months += 1

        # The net total amount of profit/ losses over the entire period
        net_profit_loss = net_profit_loss + int(row[1])

        # Average of the changes in "Profit/Losses" over the entire period
        avg_change = sum(net_profits)/len(net_profits)

    # to get the greatest increase in profits
    greatest_increase = max(net_profits)
    greatest_inc_index = net_profits.index(greatest_increase)
    greatest__inc_date = dates[greatest_inc_index]

    # to get the greatest decrease in profits
    greatest_decrease = min(net_profits)
    greatest__dec_index = net_profits.index(greatest_decrease)
    greatest__dec_date = dates[greatest__dec_index]

#Printing the analysiss output
print_all_output = (
    f"Financial Analysis\n"
    f"\n"
    f"-------------------------------------\n"
    f"\n"
    f"Total Months: {str(number_of_months)}\n"
    f"\n"
    f"Total: ${str(net_profit_loss)}\n"
    f"\n"
    f"Average Change: ${str(round(avg_change,3))}\n"
    f"\n"
    f"Greatest Increase in Profits: {greatest__inc_date} (${str(greatest_increase)})\n"
    f"\n"
    f"Greatest Decrease in Profits: {greatest__dec_date} (${str(greatest_decrease)})\n")
f"end"

print(print_all_output)

# Exporting to txt file

output_file = os.path.join('.', 'analysis', 'pyBank_output.txt')


pyBank_output = open(output_file, "w")

line1 = "Financial Analysis"
line2 = " "
line3 = "------------------------------------------"
line4 = " "
line5 = str(f"Total Months: {str(number_of_months)}")
line6 = " "
line7 = str(f"Total: ${str(net_profit_loss)}")
line8 = " "
line9 = str(f"Average Change: ${str(round(avg_change,3))}")
line10 = " "
line11 = str(f"Greatest Increase in Profits: {greatest__inc_date} (${str(greatest_increase)})")
line12 = " "
line13 = str(f"Greatest Decrease in Profits: {greatest__dec_date} (${str(greatest_decrease)})")
line14 = " "
line15 = "------------------------------------------"
line16 = "end"
pyBank_output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(
    line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12, line13, line14, line15, line16))
pyBank_output.close()


