

# 1. Input the number of eggs collected on each day of the week for the seven days of the week. You must use a loop to do this
#     a. In the input, you must say the name of the day as shown in the sample output
#         i. To do this you will use a selection within the loop. You will NOT have seven unique input statements. It will be one statement repeated 7 times with the loop iterations
eggsTotal = 0
weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
for i in range(len(weekdays)):
    # print(weekdays[i])
    dailyEggs = int(input('How many eggs did you collect on ' + weekdays[i] + '?'))
    eggsTotal += dailyEggs
route = input('What route would you like to take today? Enter M for Mountain or R for River.')
routeMiles = 0
if route == 'm':
    routeMiles += 15.13
elif route == 'r':
    routeMiles += 12.22
# print(routeMiles)
print('         Total eggs collected                ', eggsTotal)
cartons = eggsTotal // 12
print('         Total cartons made                  ', cartons)

# 2. You will input the road Farmer Suzy will take to the Farmer’s Market.
# 3. Ensure that Farmer Suzy does not enter any value less than 55 or greater than
# 550 for the number of eggs collected each day
# a. This requirement is based on the assumption that each chicken lays at
# least one egg per day and no chicken lays more than 10 eggs per day
# 4. Calculate:
# a. The total eggs collected during the week
# b. The number of cartons Farmer Suzy will cart to the Farmer’s Market
# c. The gross proceeds from the sales of eggs – remember there are four
# different rate levels (see page 1)
# d. The total expenditures Farmer Suzy has incurred for the eggs including
# gasoline for the truck
# e. The weekly profit
# 5. If all the parameters remain the same each week, can you now forecast the annual profit for Farmer Suzy?

chickenFeed = .10 * 55
coopUpkeep = .12 * 55
helper = 8.50


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

# $4 per dozen for medium eggs
# $5 per dozen for large eggs
# $6 per dozen for jumbo eggs
# $7 per dozen for uber eggs
