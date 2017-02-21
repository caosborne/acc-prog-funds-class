# 1. Input the number of eggs collected on each day of the week for the seven days of the week. You must use a loop to do this
#     a. In the input, you must say the name of the day as shown in the sample output
#         i. To do this you will use a selection within the loop. You will NOT have seven unique input statements. It will be one statement repeated 7 times with the loop iterations
eggsTotal = 0
# weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# 3. Ensure that Farmer Suzy does not enter any value less than 55 or greater than
# 550 for the number of eggs collected each day
# a. This requirement is based on the assumption that each chicken lays at
# least one egg per day and no chicken lays more than 10 eggs per day
for day in days:
        dailyEggs = int(input('How many eggs did you collect on ' + day + '? '))
        while dailyEggs < 55 or dailyEggs > 550:
            dailyEggs = int(input('Please enter a valid number for ' + day + ':( 55 <-> 550 ) '))
        else:
            eggsTotal += dailyEggs

# for i in range(len(weekdays)):
#     # print(weekdays[i])
#     dailyEggs = int(input('How many eggs did you collect on ' + weekdays[i] + '?'))
#     if dailyEggs < 55 or dailyEggs > 550:
#         # do something
#         print('There needs to be more than 55 and less 550 eggs per day!')
#         # continue
#     else:
#         eggsTotal += dailyEggs


# 2. You will input the road Farmer Suzy will take to the Farmer’s Market.
route = input('What route would you like to take today? Enter M for Mountain or R for River: ')
routeMiles = 0
if route == 'm':
    routeMiles += 15.13
elif route == 'r':
    routeMiles += 12.22
# print(routeMiles)
# a. The total eggs collected during the week
print('         Total eggs collected                ', eggsTotal)
# b. The number of cartons Farmer Suzy will cart to the Farmer’s Market
cartons = eggsTotal // 12
print('         Total cartons made                  ', cartons)

# cartonSize = ['medium', 'large', 'jumbo', 'uber']
mediumCarton = int(input('How many medium cartons did you sell: '))
largeCarton = int(input('How many large cartons did you sell: '))
jumboCarton = int(input('How many jumbo cartons did you sell: '))
uberCarton = int(input('How many uber cartons did you sell: '))

# Does the number of cartons sold need to equal the cartons I took to the market?
#  If so I need to set a check to make sure the numbers sold match the numbers taken to the market

print('  ')
print('====================================================================================')
print('  ')
# $4 per dozen for medium eggs
# $5 per dozen for large eggs
# $6 per dozen for jumbo eggs
# $7 per dozen for uber eggs
# c. The gross proceeds from the sales of eggs – remember there are four
# different rate levels (see page 1)
mediumCartonsSold = mediumCarton * 4
largeCartonsSold = largeCarton * 5
jumboCartonsSold = jumboCarton * 6
uberCartonsSold = uberCarton * 7
totalCartonSales = mediumCartonsSold + largeCartonsSold + jumboCartonsSold + uberCartonsSold

# 1. Farmer Suzy has 55 chickens
# 2. She spends $0.10 per chicken per week on chicken feed
# 3. She spends $0.12 per chicken per week on the upkeep of the chicken coop
# 4. She can take up to 500 cartons safely to the Farmers Market each week in her
# truck
# 5. Each carton holds a dozen eggs
# 6. She sells all the cartons she carries to the Market every week – nothing is ever left
# over
# 7. She pays a commission to the Austin Farmer's Market to put up her egg stall –
# this commission is 1% of the total sales for the week
# 8. Farmer Suzy has a helper who works 15 hours a week for her at $8.50 per hour
# 9. There are two ways to get to the Farmer’s Market from Suzy’s farm – the
# mountain road (15.13 miles) and the river road (12.22 miles). The river road is much shorter but is closed very often due to the threat of flooding. Yes, there are mountains around Austin!
# 10. Farmer Suzy’s truck gives an astoundingly high 6.5 MPG
# 11. Gas costs $3.99 per gallon
# 12. Net profit takes into account all revenues and all expenditures
# d. The total expenditures Farmer Suzy has incurred for the eggs including
# gasoline for the truck
weeklyChickenFeed = .10 * 55
weeklyCoopUpkeep = .12 * 55
weeklyTotalChickenMaintanence = weeklyCoopUpkeep + weeklyChickenFeed
weeklyHelperWage = 8.50 * 15
commission = totalCartonSales * .01
# milesRoundtrip = routeMiles * 2
# gallonsUsed = float(milesRoundtrip / 6.5)
# gasolineCost = gallonsUsed * 3.99
# print('  ')
# print(milesRoundtrip)
# print(format(gallonsUsed, '.2f'))
# print(gasolineCost)
# print('  ')
gasolineUsed = (( routeMiles * 2 ) / 6.5) * 3.99
totalExpenditure = commission + weeklyHelperWage + weeklyTotalChickenMaintanence + gasolineUsed
weeklyProfit = totalCartonSales - totalExpenditure
projectedAnnualProfit = weeklyProfit * 52
# e. The weekly profit
# 5. If all the parameters remain the same each week, can you now forecast the annual profit for Farmer Suzy?

print('For the week this is what your financials look like:')
print('         Total eggs collected                ', eggsTotal)
print('         Total cartons made                  ', cartons)
print('Total Expenses:')
print('         Helper Salary                       ', format(weeklyHelperWage, '.2f'))
print('         Market Fee                          ', format(commission, '.2f'))
print('         Chicken Maintenance                 ', format(weeklyTotalChickenMaintanence, '.2f'))
print('         Gasoline Used                       ', format(gasolineUsed, '.2f'))
print('         Total Expenditure                   ', format(totalExpenditure, '.2f'))
print('Total Revenue:')
print('         Egg Sales                           ', format(totalCartonSales, '.2f'))
print('Profits:')
print('         Weekly Profit                       ', format(weeklyProfit, '.2f'))
print('         Projected Annual Profit             ', format(projectedAnnualProfit, '.2f'))
