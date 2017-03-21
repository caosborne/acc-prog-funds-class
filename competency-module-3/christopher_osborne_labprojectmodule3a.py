def main():

    # richter is the Richter scale measurement
    # (typically on a scale from 1-10 as a floating point number).
    # print(format('Richter', '<20'),format('Joules', '^20'), format('TNT', '>20'))
    # print(' ')
    # print(format('6.5', '<20'),format(10 ** (( 1.5 * 6.5 ) + 4.8 ), '^20'), format((10 ** (( 1.5 * 6.5 ) + 4.8 ) * (2.390057361377 * 10 ** -7)) / 1000, '>28'))
    # print(format('9.5', '<20'),format(10 ** (( 1.5 * 9.5 ) + 4.8 ), '^20'), format((10 ** (( 1.5 * 9.5 ) + 4.8 ) * (2.390057361377 * 10 ** -7)) / 1000, '>28'))
    # print(format('5', '<20'),format(10 ** (( 1.5 * 5 ) + 4.8 ), '^20'), format((10 ** (( 1.5 * 5 ) + 4.8 ) * (2.390057361377 * 10 ** -7)) / 1000, '>28'))
    # print(format('2', '<20'),format(10 ** (( 1.5 * 2 ) + 4.8 ), '^20'), format((10 ** (( 1.5 * 2 ) + 4.8 ) * (2.390057361377 * 10 ** -7)) / 1000, '>28'))
    # print(format('7.5', '<20'),format(10 ** (( 1.5 * 7.5 ) + 4.8 ), '^20'), format((10 ** (( 1.5 * 7.5 ) + 4.8 ) * (2.390057361377 * 10 ** -7)) / 1000, '>28'))
    # print(' ')
    # print('=========================================================')
    # print(' ')

    richterValues()


    # Greeting message to user
    # print('     Rumble     Rumble     Rumble')
    # print('I think we just felt an earthquake!')
    # print(' ')

    greetingMessage()

    # if richterScale < 1 or richterScale > 10:
    #     i = 0
    # Need a loop before richterScale to come back to in the first if statement after they user is promtped that answer is incorrect.
    counter = 0
    while counter < 3:
        richterScale = inputRichter()
        # Set variable to an input asking the user how big they think that earthquake was on a richter scale
        # richterScale = float(input('How big do you think that was on the Richter Scale? (Usually a Richter Scale is measured from 1-10) '))
        print(' ')
        print('=========================================================')
        print(' ')
        # i += 1
        # Need to set a parameter of the input not being less than 1 or greater than 10
        # User will get three chances to input a correct number if not the program aborts
            # This will need to be a loop that checks if number was input correctly.
            # If not ask again
        if richterScale < 1 or richterScale > 10:
            print('That is not a valid Richter Scale measurement.')
            print('Please try putting in a correct Richter Scale value.')
            print('  ')
            print('  ')
            # richterScale = float(input('How big do you think that was on the Richter Scale? (Usually a Richter Scale is measured from 1-10)'))
            counter += 1
        else:
            # There needs to be parameters with prints that same some comment
                # 1-4 "You call that an earthquake?"
                # 5-8 "That's not a earthquake"
                # 9-10 "Now that's an earthquake!"
            richterComments(richterScale)
            # if richterScale <= 4:
            #     print('You call that an earthquake?')
            #     print('  ')
            # elif richterScale > 4 and richterScale <= 8:
            #     print('That\'s not a earthquake!')
            #     print('  ')
            # elif richterScale > 8 and richterScale <= 10:
            #     print('Now that\'s an earthquake!')
            #     print('  ')
            # print the value the user input and then run the measurements
            print('A Richter Scale value of ', richterScale, ' results in the following: ')

            # create a variable with the equation of energy(joules) and explodedTNT
                # Energy = 10^(1.5*richter)+4.8
                # 1 joule = 2.390057361377 * 10-7 kilogram of TNT
                # To raise a number to a power, use the ** operator. For example:
                # print( "The number 10 raised to the power 1.5 is", 10**1.5 )
            # energy = 10 ** (( 1.5 * richterScale ) + 4.8 )
            energy = energyCalc(richterScale)
            explodedTNT = explodedTNTCalc(energy)

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

            # energySN = format(energy, '.2e')
            # explodedTNT_SN = format(explodedTNT, '.2e')
            energySN = scientificNotationEnergy(energy)
            explodedTNT_SN = scientificNotationTNT(explodedTNT)

            # print the results from the scientific notation and confirm they're correct with same website as before.
            print('     In joules: ', energySN)
            print('     Tons of TNT exploded: ', explodedTNT_SN)
            break
    else:
        print('Clearly the earthquake rattled your brain and you have entered an incorrect Richter Scale value 3 times. Goodbye!')




def richterValues():
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

def greetingMessage():
    # Greeting message to user
    print('     Rumble     Rumble     Rumble')
    print('I think we just felt an earthquake!')
    print(' ')

def inputRichter():
    richterScale = float(input('How big do you think that was on the Richter Scale? (Usually a Richter Scale is measured from 1-10) '))
    return richterScale

def richterComments(num):
    if num <= 4:
        print('You call that an earthquake?')
        print('  ')
    elif num > 4 and num <= 8:
        print('That\'s not a earthquake!')
        print('  ')
    elif num > 8 and num <= 10:
        print('Now that\'s an earthquake!')
        print('  ')

def energyCalc(num):
    energy = 10 ** (( 1.5 * num ) + 4.8 )
    return energy

def explodedTNTCalc(num):
    explodedTNT = (num * (2.390057361377 * 10 ** -7)) / 1000
    return explodedTNT

def scientificNotationEnergy(num):
    energySN = format(num, '.2e')
    return energySN

def scientificNotationTNT(num):
    explodedTNT_SN = format(num, '.2e')
    return explodedTNT_SN


main()
