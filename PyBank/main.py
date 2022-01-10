import os
import csv



#specify file to write results to
output_path=os.path.join("output.csv")

#opeon file using "write" mode. Specify variable to hold the contents
with open(output_path, 'w') as csvfile:

    #initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    #write the the first row (column headers)
    csvwriter.writerow(['Financial Analysis'])

    #write the second row
    csvwriter.writerow(['Total Months: '])
    csvwriter.writerow(['Total:  '])
    csvwriter.writerow(['Average Change: '])
    csvwriter.writerow(['Greatest Increase in Profits:  '])
    csvwriter.writerow(['Greatest Decrease in Profits:  '])
  



