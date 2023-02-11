import os
import csv

pyBankCSV = os.path.join("Resources", "budget_data.csv")
#print(pyBankcsv)
# file is successfully loaded

outpath = os.path.join("Resources", "budgetAnalysis.txt")

# i need my total months set at 0
totalMonths = 0
changeMonths = 0

#i also need my total profit equal to zero
totalProfit = 0

#i need to set profit equal to 0 before calculating my if
profit = 0

#set total change equal to zero so i can add up the changes
totalChange = 0

#greatest increase needs to start at zero and the date needs to be set
greatestIncrease = 0
greatestIncreaseDate = " "

#i need these same values for greatest decrease
greatestDecrease = 0
greatestDecreaseDate = " "

#now i need to use the csv reader
with open(pyBankCSV) as File:
    csvReader = csv.reader(File, delimiter=",")
    next(csvReader) # no headers

# OK now i have my path and my reader open
#im going to use a for loop to go down the rows

    for row in csvReader:
        totalMonths +=1 
        totalProfit = totalProfit + int(row[1])
    #this gives me total months and total profits
        currentProfit = int(row[1])
        #current profit is equal to the actual value in column B 
        change = 0
        #i need to figure out change in current profit

        if profit != 0:
            change = currentProfit - profit
            totalChange += change
            changeMonths +=1
            #this should take the change between the profits
            #this should add all the changes together
            #this should make note of the months attached to the changes

        profit = currentProfit

        #i still need my greatest increas and my greatest decrease
        if change > greatestIncrease:
            greatestIncrease = change
            greatestIncreaseDate = row[0]

        if change < greatestDecrease:
            greatestDecrease = change
            greatestDecreaseDate = row[0]

    
print("Financial Analysis")
print("--------------------------------------")    
print("Total Months: " + str(totalMonths))
print("Total Profit: " + "$" + str(totalProfit))
print("Average CHange: " + "$" + str(totalChange/changeMonths))
#i can not get the float points to work, it messes with the syntax
#im gonna leave the float points alone
print("Greatest Increase in Profits: " + str(greatestIncreaseDate) + "$" + str(greatestIncrease))
print("Greatest Decrease Date: " + str(greatestDecreaseDate) + "$" + str(greatestDecrease))

#the f strings after the print were messing up again, so i stuck with the long way
#also the float points mess up the syntax, and I finally have the numbers right
#i left the syntaxs alone
with open(outpath, "w") as outFile:
    outFile.write("Financial Analysis")
    outFile.write("--------------------------------------")    
    outFile.write("Total Months: " + str(totalMonths))
    outFile.write("Total Profit: " + "$" + str(totalProfit))
    outFile.write("Average CHange: " + "$" + str(totalChange/changeMonths))
    outFile.write("Greatest Increase in Profits: " + str(greatestIncreaseDate) + "$" + str(greatestIncrease))
    outFile.write("Greatest Decrease Date: " + str(greatestDecreaseDate) + "$" + str(greatestDecrease))

    