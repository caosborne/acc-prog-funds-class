# Print a welcome message
# Prompt user for how many of each coin they'd like to deposit and store these into variables
print(" Hey welcome to Chris's coin machine! ")
halfDollars = float(input('How many half dollars would you like to deposit?'))
quarters = float(input('How many quarters would you like to deposit?'))
dimes = float(input('How many dimes would you like to deposit?'))
nickels = float(input('How many nickels would you like to deposit?'))
pennies = float(input('How many pennies would you like to deposit?'))

# Convert the number of coins deposited to dollar amount
totalHalfDollars = halfDollars * .5
totalQuarters = quarters * .25
totalDimes = dimes * .1
totalNickels = nickels * .05
totalPennies = pennies * .01

# Print a message letting the user know how many coins they deposited and how much that converted to in dollars in 2 decimal places.
print("You've deposited: ", halfDollars, " Half Dollars worth: $", format(totalHalfDollars, '.2f'))
print("You've deposited: ", quarters, " Quarters worth: $", format(totalQuarters, '.2f'))
print("You've deposited: ", dimes, " Dimes worth: $", format(totalDimes, '.2f'))
print("You've deposited: ", nickels, " Nickels worth: $", format(totalNickels, '.2f'))
print("You've deposited: ", pennies, " Pennies worth: $", format(totalPennies, '.2f'))

# create a variable that stores that total amount of all coins deposited
totalDeposit = float(format(totalHalfDollars + totalQuarters + totalDimes + totalNickels + totalPennies, '.2f'))
# totalDeposit = totalHalfDollars + totalQuarters + totalDimes + totalNickels + totalPennies

# Print the total amount with a message to the user.
print("You're total deposit amount is: $", format(totalDeposit, '.2f'))

# Set a variable for the processing fee and print a message letting the user know how much the fee is
processingFee = float(format(totalDeposit * .0477, '.2f'))
print("You're processing fee is: $", processingFee)

#  Set a variable for the coin tax for the machine and print a message letting the user know how much it is
coinTax = totalDeposit * .01
print("You're machine coin tax is: $", coinTax)

# Set a variable that sums the total of the tax and fee and print a message letting the user know
totalFees = float(coinTax + processingFee)
print("You're total tax & fees are: $", totalFees)

# Set a variable with the totalDeposit minus the totalFees and print how much in total the user will get back in cash.
totalCashReturn = float(totalDeposit - totalFees)
print("The total cash returned is: $", totalCashReturn)
