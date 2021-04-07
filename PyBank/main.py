#imports
import os
import csv

# set the path for the CSV file 

PyBankcsv = os.path.join("Resources", "budget_data.csv")

#  lists to store data. 

profit = []
monthlyChanges = []
date = []

# set variables 
 
count = 0
totalChangeProfits = 0
totalProfit = 0
initialProfit = 0

# open the CSV file

with open(PyBankcsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

    
    for row in csvreader:    
      count = count + 1 

      date.append(row[0])

      profit.append(row[1])
      totalProfit = totalProfit + int(row[1])

      finalProfit = int(row[1])
      monthlyChangeProfits = finalProfit - initialProfit

      monthlyChanges.append(monthlyChangeProfits)

      totalChangeProfits = totalChangeProfits + monthlyChangeProfits
      initialProfit = finalProfit

      # average change in profits
      averageChangeProfits = (totalChangeProfits/count)
      
      # find the max and min changes
      greatestIncreaseProfits = max(monthlyChanges)
      greatestDecreaseProfits = min(monthlyChanges)

      increaseDate = date[monthlyChanges.index(greatestIncreaseProfits)]
      decreaseDate = date[monthlyChanges.index(greatestDecreaseProfits)]
      
    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(totalProfit))
    print("Average Change: " + "$" + str(int(averageChangeProfits)))
    print("Greatest Increase in Profits: " + str(increaseDate) + " ($" + str(greatestIncreaseProfits) + ")")
    print("Greatest Decrease in Profits: " + str(decreaseDate) + " ($" + str(greatestDecreaseProfits)+ ")")
    print("----------------------------------------------------------")

with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(totalProfit) +"\n")
    text.write("    Average Change: " + '$' + str(int(averageChangeProfits)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increaseDate) + " ($" + str(greatestIncreaseProfits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decreaseDate) + " ($" + str(greatestDecreaseProfits) + ")\n")
    text.write("----------------------------------------------------------\n")
