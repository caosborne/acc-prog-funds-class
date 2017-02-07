# richter is the Richter scale measurement
# (typically on a scale from 1-10 as a floating point number).

# Greeting message to user
print('     Rumble     Rumble     Rumble')
print('I think we just felt an earthquake!')
print(' ')

# Set variable to an input asking the user how big they think that earthquake was on a richter scale
richterScale = float(input('How big do you think that was on the Richter Scale?'))
print(' ')
print('=========================================================')
print(' ')

# print the value the user input and then run the measurements
print('A Richter Scale value of ', richterScale, ' results in the following: ')

# create a variable with the equation of energy(joules) and explodedTNT
    # Energy = 10^(1.5*richter)+4.8
    # 1 joule = 2.390057361377 * 10-7 kilogram of TNT
    # To raise a number to a power, use the ** operator. For example:
    # print( "The number 10 raised to the power 1.5 is", 10**1.5 )
energy = 10 ** (( 1.5 * richterScale ) + 4.8 )
explodedTNT = (energy * (2.390057361377 * 10 ** -7)) / 1000

# print the results from the variables set of the equations for energy(joules) and explodedTNT
# check these outputs with the website given in instructions to confirm they're correct
print('     In joules: ', energy)
print('     Tons of TNT exploded: ', explodedTNT)

print(' ')
print('=========================================================')
print(' ')

# print the same message from above letting the user know what richter scale measuremen they chose and now let them know this will be in scientific notation
print('A Richter Scale value of ', richterScale, ' results in the following fancy scientific notation: ')

# set variables for the energy and explodedTNT variables but in scientific notation
    # To indicate scientific notation in Python, use the format specifier.
    # Example: print(format(354813389233576.06, ‘.2e’))
energySN = format(energy, '.2e')
explodedTNT_SN = format(explodedTNT, '.2e')

# print the results from the scientific notation and confirm they're correct with same website as before.
print('     In joules: ', energySN)
print('     Tons of TNT exploded: ', explodedTNT_SN)
