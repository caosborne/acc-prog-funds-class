def main():
    # Greeting message to user
    greetingMessage()

    # Need a loop before richterScale to come back to in the first if statement after they user is promtped that answer is incorrect.
    counter = 0
    while counter < 3:
        # Set variable to an input asking the user how big they think that earthquake was on a richter scale
        richterScale = inputRichter()
        print(' ')
        print('=========================================================')
        print(' ')

        # Need to set a parameter of the input not being less than 1 or greater than 10
        # User will get three chances to input a correct number if not the program aborts
            # This will need to be a loop that checks if number was input correctly.
            # If not ask again
        if richterScale < 1 or richterScale > 10:
            print('That is not a valid Richter Scale measurement.')
            print('Please try putting in a correct Richter Scale value.')
            print('  ')
            print('  ')
            counter += 1
        else:
            # There needs to be parameters with prints that same some comment
                # 1-4 "You call that an earthquake?"
                # 5-8 "That's not a earthquake"
                # 9-10 "Now that's an earthquake!"
            richterComments(richterScale)

            energy = energyCalc(richterScale)
            explodedTNT = explodedTNTCalc(energy)

            firstLine = '========================================================='
            secondLine = 'You entered ' + str(richterScale) + ' and a Richter Scale value of ' + str(richterScale) + ' results in the following: '
            thirdLine = '     In joules: ' + str(energy)
            fourthLine = '     Tons of TNT exploded: ' + str(explodedTNT)

            richterValues(firstLine, secondLine, thirdLine, fourthLine)
            break
    else:
        print('Clearly the earthquake rattled your brain and you have entered an incorrect Richter Scale value 3 times. Goodbye!')

def richterValues(one, two, three, four):
    try:
        # 2 Read the values from the richters.txt file into a list using the readlines() method
        infile = open('richters.txt', 'r')
        richterValues = infile.readlines()
        infile.close()
        # 3 Sort the list using the sort method for example mylist.sort()
        richterValues.sort()
        # 4 Create a new list using for example newlist = []
        newList = []
        # create a loop that iterates through the list to make them floats.
        i = 0
        while i < len(richterValues):
            # 5 append all the values you read from the file into newlist
            newList.append(float(richterValues[i].rstrip('\n')))
            i += 1

        outfile = open('earthquakesChristopherOsborne2.txt', 'a')
        
        value = 0
        for value in newList:
           richter = value
           energy = energyCalc(richter)
           eTNT = explodedTNTCalc(richter)

           outfile.write(str(richter) + '\t\t\t\t' + str(energy) + '\t\t\t\t' + str(eTNT) + '\n' + '\n')

        outfile.write(one + '\n' + two + '\n' + three + '\n' + four)
        outfile.close()
    except IOError:
        print('An error occurred trying to read the input file. Please try again!')

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
    # Energy = 10^(1.5*richter)+4.8
    # To raise a number to a power, use the ** operator. For example:
    # print( "The number 10 raised to the power 1.5 is", 10**1.5 )
    energy = 10 ** (( 1.5 * num ) + 4.8 )
    return energy

def explodedTNTCalc(num):
    # 1 joule = 2.390057361377 * 10-7 kilogram of TNT
    explodedTNT = (num * (2.390057361377 * 10 ** -7)) / 1000
    return explodedTNT

def scientificNotationEnergy(num):
    energySN = format(num, '.2e')
    return energySN

def scientificNotationTNT(num):
    explodedTNT_SN = format(num, '.2e')
    return explodedTNT_SN

main()
