#Rob started his own small business and named it Rob The Landscape Guy. No, Rob did not realize that the missing comma could be detrimental to his well being!

#Rob mows lawns and offers fertilizing service. 

#I will test your programs with the following yard sizes: 500, 200, 3500 with both yes and no for the fertilizer

#The user gets three chances to enter the correct value. If in three tries the user has not entered a correct value the program should issue an error message and end.
counter = 0
while counter < 3:
	print('Welcome to Rob The Landscape Guy\'s Invoice System.')
	#Input the lawn size from the user
	yardSize = float(input('Please enter your yard size. Your yard must be 100 square feet or more. '))
	mowingRate = 0
	fertilizerCost = 0.00
	#The user cannot enter a lawn size less than 100 square feet
	if yardSize < 100:
		print('The yard size is too small please try again.')
		counter += 1
	else:
		#Input a yes or no choice for fertilizer from the user
		#For the fertilizing service, Rob charges an extra $15 regardless of yard size.
		fertilizer = input('Would you like you\'re yard fertilized? Type y for yes or any other key for no. ')
		if fertilizer == 'y':
			fertilizerCost = float(15.00)
		else:
			fertilizerCost = float(0.00)
			
		#print(fertilizerCost)
		#Calculate the total charge for the lawn service.
		#His normal rate is $40 per mowing for a normal size yard. 
			#For a yard that is over 3000 square feet he adds on 25% to this rate. 
			#For a yard smaller than 300 square feet he offers a 10% discount. 
		if yardSize < 300:
			mowingRate = 40 * .9
		elif yardSize > 3000:
			mowingRate = 40 * 1.25
		else:
			mowingRate = 40
			
		print('You\'re mowing charges based on your yard size of ', yardSize, ' are as follows:')
		print('Mowing Charge: $', format(mowingRate, '.2f'))
		print('Fertilizer Charge: $', format(fertilizerCost, '.2f'))
		totalCost = mowingRate + fertilizerCost
		print('Total Charge: $', format(totalCost, '.2f'))
		break
else:
	print('You have entered too small of a yard 3 times and the program has ended!')
