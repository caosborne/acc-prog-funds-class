# Sam HouseFlipper purchased a house on Cesar Chavez street on August 1, 2016. The following were the details of the purchase:
    # Purchase price of the house: $123,000
    # Closing costs: $2,111
    # Realtor commission: 4.5% of the sale price
    # Sam spent $10,999 fixing up this house.
purchasePrice = 123000
closingCosts = 2111
buyingRealtorCommission = float(purchasePrice * .045)
fixUpCost = 10999

print('Purchased House on Aug. 1, 2016 with these costs:')
print('     Purchase Price: $', purchasePrice)
print('     Closing Costs: $', closingCosts)
print('     Realtor Commission: $', format(buyingRealtorCommission, '.2f'))
print('     Fix Up Costs: $', fixUpCost)

# On August 29, 2016 Sam sold the house. The following were the details of the sale:
    # Sale price of the house: $156,000
    # Realtor commission on sale: 3% of the sale price
    # Carpet allowance to buyer: $1100
soldPrice = 156000
sellingRealtorCommission = float(soldPrice * .03)
carpetAllowance = 1100
print(' ')
print('Sold House on Aug. 29, 2016 with these figures:')
print('     Sold Price: $', soldPrice)
print('     Realtor Commission: $', format(sellingRealtorCommission, '.2f'))
print('     Carpet Allowance: $', carpetAllowance)

# Write a program that displays the following:
    # The purchase price of the house
    # Total closing costs on purchase
    # Total realtor commission on purchase
    # The money spent on fixing up the house
    # The sale price of the house
    # Total realtor commission on sale
    # The total profit or loss that Sam made on this house
totalExpenses = purchasePrice + closingCosts + fixUpCost + buyingRealtorCommission + carpetAllowance + sellingRealtorCommission
profitLossStatement = soldPrice - totalExpenses
print(' ')
print("Sam's Total Expenses for the house were: $", format(totalExpenses, '.2f'))
print('')
print('Sam made a profit of: $', format(profitLossStatement, '.2f'), 'after selling the house and recovering the cost of expenses.')
