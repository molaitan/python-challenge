import os
import csv

#set path for financial data file
csvpath = os.path.join("Resources", "budget_data.csv")

#lists to store data from data file
date=[]
profit_loss=[]
changes=0
previous_row=0
total=[]

#open financial data file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #skip header row
    next(csvreader)
    #loop through each row to find change between each period
    for row in csvreader:

        changes= int(row[1])-previous_row
        previous_row=int(row[1])

        date.append(row[0])
        profit_loss.append(changes)
        total.append(int(row[1]))

    #remove first value of profit_loss list since value is not a true change value
    profit_loss.pop(0)

    #make financial analysis for output file
    total_mo=len(date)
    total_money=sum(total)
    average_change= sum(profit_loss) /(total_mo-1)
    greatest_increase=max(profit_loss)
    greatest_decrease= min(profit_loss)
    increase_date=date[profit_loss.index(greatest_increase)+1]
    decrease_date=date[profit_loss.index(greatest_decrease)+1]

    #print results to terminal
    # print(total_mo)
    # print(total_money)
    # print(greatest_increase)
    # print(greatest_decrease)
    # print(increase_date)
    # print(decrease_date)

    print("Financial Analysis")
    print("-----------------------------")
    print(f"Total Months: {total_mo}\n")
    print(f"Total Money: ${total_money}\n")
    print(f"Average Change:  ${average_change:.2f}\n")
    print(f"Greatest Increase in Profits:  {increase_date} (${greatest_increase})\n")
    print(f"Greatest Decrease in Profits:  {decrease_date} (${greatest_decrease})\n" )


#specify file to write results to
output_path = os.path.join("Analysis","output.txt")

output = (  f"Financial Analysis\n"
            f"------------------------------\n"
            f"Total Months: {total_mo}\n"
            f"Total Money: ${total_money}\n"
            f"Average Change:  ${average_change:.2f}\n"
            f"Greatest Increase in Profits:  {increase_date} (${greatest_increase})\n"
            f"Greatest Decrease in Profits:  {decrease_date} (${greatest_decrease})\n" )

#write output data to text file
with open(output_path, "w") as txt_file:
   txt_file.write(output)


    



