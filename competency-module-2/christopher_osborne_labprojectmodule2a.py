# richter is the Richter scale measurement
# (typically on a scale from 1-10 as a floating point number).
print(format('Richter', '<20'),format('Joules', '^20'), format('TNT', '>20'))
print(' ')
print(format('6.5', '<20'),format(10 ** (( 1.5 * 6.5 ) + 4.8 ), '^20'), format((10 ** (( 1.5 * 6.5 ) + 4.8 ) * (2.390057361377 * 10 ** -7)) / 1000, '>28'))
print(format('9.5', '<20'),format(10 ** (( 1.5 * 9.5 ) + 4.8 ), '^20'), format((10 ** (( 1.5 * 9.5 ) + 4.8 ) * (2.390057361377 * 10 ** -7)) / 1000, '>28'))
print(format('5', '<20'),format(10 ** (( 1.5 * 5 ) + 4.8 ), '^20'), format((10 ** (( 1.5 * 5 ) + 4.8 ) * (2.390057361377 * 10 ** -7)) / 1000, '>28'))
print(format('2', '<20'),format(10 ** (( 1.5 * 2 ) + 4.8 ), '^20'), format((10 ** (( 1.5 * 2 ) + 4.8 ) * (2.390057361377 * 10 ** -7)) / 1000, '>28'))
print(format('7.5', '<20'),format(10 ** (( 1.5 * 7.5 ) + 4.8 ), '^20'), format((10 ** (( 1.5 * 7.5 ) + 4.8 ) * (2.390057361377 * 10 ** -7)) / 1000, '>28'))

print(' ')
print('=========================================================')
print(' ')

# Greeting message to user
print('     Rumble     Rumble     Rumble')
print('I think we just felt an earthquake!')
print(' ')

# Need a loop before richterScale to come back to in the first if statement after they user is promtped that answer is incorrect.

# Set variable to an input asking the user how big they think that earthquake was on a richter scale
richterScale = float(input('How big do you think that was on the Richter Scale? (Usually a Richter Scale is measured from 1-10)'))
print(' ')
print('=========================================================')
print(' ')

# Need to set a parameter of the input not being less than 1 or greater than 10
# User will get three chances to input a correct number if not the program aborts
    # This will need to be a loop that checks if number was input correctly.
    # If not ask again
if richterScale < 1 or richterScale > 10:
    i = 0
    print('That is not a valid Richter Scale measurement.')
    while i < 3:
        i += 1
        if i < 3:
            print('Please try putting in a correct Richter Scale value.')
            # richterScale = float(input('How big do you think that was on the Richter Scale? (Usually a Richter Scale is measured from 1-10)'))
        else:
            print('You have entered an incorrect number 3 times. Goodbye!')
else:
    # There needs to be parameters with prints that same some comment
        # 1-4 "You call that an earthquake?"
        # 5-8 "That's not a earthquake"
        # 9-10 "Now that's an earthquake!"
    if richterScale <= 4:
        print('You call that an earthquake?')
        print('  ')
    elif richterScale > 4 and richterScale <= 8:
        print('That\'s not a earthquake!')
        print('  ')
    elif richterScale > 8 and richterScale <= 10:
        print('Now that\'s an earthquake!')
        print('  ')
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
