
import csv
import os

csvpath = os.path.join("Resources", "budget_data.csv")


#The total number of months included in the dataset

month = []
year = []

with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    for row in csvreader:
        split_date = row[0].split("-")
        month =  month + [split_date[0]]
        year = year + [split_date[1]]

unique_month = []
for i in month:
    if i not in unique_month: 
        unique_month.append(i)
print(unique_month)


#Count the total number of months included in the dataset

Jan_count=month.count("Jan")
Feb_count=month.count("Feb")
Mar_count=month.count("Mar")
Apr_count=month.count("Apr")
May_count=month.count("May")
Jun_count=month.count("Jun")
Jul_count=month.count("Jul")
Aug_count=month.count("Aug")
Sep_count=month.count("Sep")
Oct_count=month.count("Oct")
Nov_count=month.count("Nov")
Dec_count=month.count("Dec")
month_list=[Jan_count,Feb_count,Mar_count,Apr_count,May_count,Jun_count,Jul_count,Aug_count,Sep_count,Oct_count,Nov_count,Dec_count]
month_count=sum(month_list)
print(month_count)
:


#The net total amount of "Profit/Losses" over the entire period

with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    total = sum(int(row[1]) for row in csvreader)
print(total)


#The average of the changes in "Profit/Losses" over the entire period

average=total/month_count
print(average)


#The greatest increase in profits (date and amount) over the entire period

def print_maxdate():
    max_date = str(row[0])
    
with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    max_change = max(float(row[1]) for row in csvreader)
    max_change_dollars = "${:,.2f}".format(max_change)


    with open(csvpath,'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)
        for row in csvreader:
            if max_change == float(row[1]):
                max_date = str(row[0])
print("The greatest increase in profits was in", max_date, max_change_dollars)



#The greatest decrease in losses (date and amount) over the entire period

def print_maxdate():
    min_date = str(row[0])
    
with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    min_change = min(float(row[1]) for row in csvreader)
    min_change_dollars = "${:,.2f}".format(min_change)

    with open(csvpath,'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)
        for row in csvreader:
            if min_change == float(row[1]):
                min_date = str(row[0])
print("The greatest decrease in losses was in", min_date, min_change_dollars)



# Generate Paragraph Analysis Output
output = (
    f"\nFinancial Analysis\n"
    f"-----------------\n"
    f"Total Months: {month_count}\n"
    f"Average  Change: {average}\n"
    f"Greatest increase in profits was in {max_date} ({max_change_dollars})\n"
    f"Greatest decrease in losses was in {min_date} ({min_change_dollars})\n")

# Print all of the results (to terminal)
print(output)

file_to_output = os.path.join("analysis", "PyBank_output.txt")

# Save the results to analysis text file
with open(file_to_output, "a") as txt_file:
    txt_file.write(output)

