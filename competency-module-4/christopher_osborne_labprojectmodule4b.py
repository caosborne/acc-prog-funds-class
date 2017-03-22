def main():
    # For this lab you will need to:
    # 1. Write a function to input the cost of the airline ticket. You will write one function that will be called four times in a loop.
    airlineTicketTotal = 0
    baggageCostTotal = 0
    names = ['Missy Musician', 'A-A-Ron', 'Solar Steve', 'Crazy Kate']

    for name in names:
            airlineTicket = airlineTicketCost(name)
            # 2. Write a function that will ask for the baggage weight of each band member. Again, you will write one function that will be called four times in the same loop as above.
            baggageWeightInput = baggageWeight()
            # 3. Write a function that will calculate the excess baggage rates for each band member. It will be called four times in the same loop as the first two inputs.
            baggageCost = baggageWeightCost(baggageWeightInput)
            airlineTicketTotal += airlineTicket
            baggageCostTotal += baggageCost
            print(' ')

    # Important Note: Within the loop, you will keep a running total of the airline tickets and baggage charges.
    # 4. Write a function that will calculate the total costs and return the total cost value.
        # a. Home rental: $2000
        # b. Van rental: $500
        # c. Per diem rate: $110 per band member
    homeRental = 2000
    vanRental = 500
    perDiem = 110
    perDiemTotal = perDiemCosts(perDiem)

    # 5. You will need to write a function that will input the number of each type of
    # merchandise item sold. This function should only have two lines of code: one line to take input and the other to return this input out to the calling function. Again, one function called multiple times.
    tShirt = 'T-Shirts'
    toteBag = 'Tote Bags'
    bobbleheadDolls = 'Bobblehead Dolls'
    tShirtsSold = numberMerchItemSold(tShirt)
    toteBagsSold = numberMerchItemSold(toteBag)
    bobbleheadDollsSold = numberMerchItemSold(bobbleheadDolls)
    print(' ')
    print('================================================================================')
    print(' ')

    # 6. Write a function that will calculate the total values of the items sold.
        # a. Total dollar value of all merchandise sold:
            # i. T-shirts....................$22 each
            # ii. Tote Bags.................$18 each
            # iii. Bobblehead dolls.....$25 each (most popular item!)
    tShirtPrice = 22
    toteBagPrice = 18
    bobbleheadDollsPrice = 25
    tShirtRev = merchSold(tShirtsSold, tShirtPrice)
    toteBagRev = merchSold(toteBagsSold, toteBagPrice)
    bobbleheadDollRev = merchSold(bobbleheadDollsSold, bobbleheadDollsPrice)

    # 7. Write a function that calculate the total revenues and return the total revenue
    # value.
    totalMerchRev = totalMerchSold(tShirtRev, toteBagRev, bobbleheadDollRev)

        # b. Honorarium paid by SXSW
        # c. SXSW will pay the band an honorarium of $5500
    honorariumSXSW = 5500

    # 8. The band pays 2.5% of the total revenues on merchandise as credit card
    # processing fee. Write a function that will calculate this fee.
    creditCardProcessingFee = creditCardTxFees(totalMerchRev)

    # 9. Write a function that will print all the costs the band has incurred and all the
    # revenues the band has generated – please see the sample output.
    totalTripCosts = totalCosts(airlineTicketTotal, baggageCostTotal, homeRental, vanRental, perDiemTotal, creditCardProcessingFee)
    totalTripRevenue = totalRevenue(totalMerchRev, honorariumSXSW)
    formatted2DecAirline = format(airlineTicketTotal, '.2f')
    formatted2DecBaggage = format(baggageCostTotal, '.2f')
    formatted2DecHomeRental = format(homeRental, '.2f')
    formatted2DecVanRental = format(vanRental, '.2f')
    formatted2DecPerDiemTotal = format(perDiemTotal, '.2f')
    formatted2DecCCFee = format(creditCardProcessingFee, '.2f')
    formatted2DecTotalTripCosts = format(totalTripCosts, '.2f')
    formatted2DecMerchRev = format(totalMerchRev, '.2f')
    formatted2DecHonorarium = format(honorariumSXSW, '.2f')
    formatted2DecTotalTripRev = format(totalTripRevenue, '.2f')


    print('For SXSW your financials look like: ')
    totalPrintout(formatted2DecAirline, formatted2DecBaggage, formatted2DecHomeRental, formatted2DecVanRental, formatted2DecPerDiemTotal, formatted2DecCCFee, formatted2DecTotalTripCosts, formatted2DecMerchRev, formatted2DecHonorarium, formatted2DecTotalTripRev)
    print('******************** You Rocked the show!! ********************')


def airlineTicketCost(string):
    airCost = float(input('Hey there ' + string + '! How much did your airline ticket cost? '))
    return airCost

def baggageWeight():
    weight = float(input('How much did your baggage weigh? '))
    return weight

def baggageWeightCost(num):
    # d. Excess baggage rate: $4.25 for each pound above 50 pounds
    cost = ( num - 50 ) * 4.25
    return cost

def perDiemCosts(num):
    perDiem = (num * 7) * 4
    return perDiem

def totalCosts(num1, num2, num3, num4, num5, num6):
    totalCosts = num1 + num2 + num3 + num4 + num5 + num6
    return totalCosts

def numberMerchItemSold(string):
    merchItemsSold = int(input('How many ' + string + ' did you sell? '))
    return merchItemsSold

def merchSold(num1, num2):
    merchSold = num1 * num2
    return merchSold

def totalMerchSold(num1, num2, num3):
    totalRev = num1 + num2 + num3
    return totalRev

def creditCardTxFees(num):
    fees = num * .025
    return fees

def totalRevenue(num1, num2):
    revenue = num1 + num2
    return revenue

def totalPrintout(num1, num2, num3, num4, num5, num6, num7, num8, num9, num10):
    print('   ', format('Item', '<20'), format('Cost', '>20'))
    print('   ', format('Airline: ', '<20'), format(num1, '>20'))
    print('   ', format('Baggage: ', '<20'), format(num2, '>20'))
    print('   ', format('Home Rental: ', '<20'), format(num3, '>20'))
    print('   ', format('Van Rental: ', '<20'), format(num4, '>20'))
    print('   ', format('Per Diem Total: ', '<20'), format(num5, '>20'))
    print('   ', format('Credit Card Fee: ', '<20'), format(num6, '>20'))
    print('   ', format('Total Trip Costs: ', '<20'), format(num7, '>20'))
    print(' ')
    print('   ', format('Item', '<20'), format('Revenue', '>20'))
    print('   ', format('Merchandise: ', '<20'), format(num8, '>20'))
    print('   ', format('Honorarium: ', '<20'), format(num9, '>20'))
    print('   ', format('Total Revenue: ', '<20'), format(num10, '>20'))
    print(' ')

main()
