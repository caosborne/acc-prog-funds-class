def main():

    # richter is the Richter scale measurement
    # (typically on a scale from 1-10 as a floating point number).
    # richterValues()

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
            # richterComments(richterScale)

            # create a variable with the equation of energy(joules) and explodedTNT
            energy = energyCalc(richterScale)
            explodedTNT = explodedTNTCalc(energy)
            energy = str(energy)
            explodedTNT = str(explodedTNT)
            # print the results from the variables set of the equations for energy(joules) and explodedTNT
            # check these outputs with the website given in instructions to confirm they're correct
            # print the value the user input and then run the measurements
            richterScale = str(richterScale)
            # print('A Richter Scale value of ' + richterScale + ' results in the following: ')
            # print('     In joules: ' + energy)
            # print('     Tons of TNT exploded: ' + explodedTNT)
            #
            # print(' ')
            # print('=========================================================')
            # print(' ')
            richterStrings = [' ', '=========================================================', ' ', 'A Richter Scale value of ' + richterScale + ' results in the following: ', '     In joules: ' + energy, '     Tons of TNT exploded: ' + explodedTNT]

            richterValues(richterStrings)

            # print the same message from above letting the user know what richter scale measuremen they chose and now let them know this will be in scientific notation
            # print('A Richter Scale value of ', richterScale, ' results in the following fancy scientific notation: ')

            # set variables for the energy and explodedTNT variables but in scientific notation
                # To indicate scientific notation in Python, use the format specifier.
                # Example: print(format(354813389233576.06, ‘.2e’))
            # energySN = scientificNotationEnergy(energy)
            # explodedTNT_SN = scientificNotationTNT(explodedTNT)

            # print the results from the scientific notation and confirm they're correct with same website as before.
            # print('     In joules: ', energySN)
            # print('     Tons of TNT exploded: ', explodedTNT_SN)
            break
    else:
        print('Clearly the earthquake rattled your brain and you have entered an incorrect Richter Scale value 3 times. Goodbye!')

def richterValues(strings):
    try:
        infile = open('richters.txt', 'r')
        richterValues = infile.readlines()
        infile.close()

        # create a loop that iterates through the list to make them floats.
        i = 0
        while i < len(richterValues):
            richterValues[i] = float(richterValues[i].rstrip('\n'))
            i += 1

        richterValues = sorted(richterValues)

        # richter is the Richter scale measurement
        # (typically on a scale from 1-10 as a floating point number).
        richterOutput = []

        n = 0
        while n < len(richterValues):
            conversions = richterValues[n], 10 ** (( 1.5 * richterValues[n] ) + 4.8 ), (10 ** (( 1.5 * richterValues[n] ) + 4.8 ) * (2.390057361377 * 10 ** -7)) / 1000
            # conversions = str(conversions)
            # conversions = list(conversions)
            # print(conversions)
            richterOutput.append(conversions)
            # richterOutput.append(strings)
            # richterOutput = conversions

            n += 1
            # print(conversions)

        # print(richterOutput + strings)
        # print(richterOutput)
        # print(' ')
        # print(strings)
        richterOutput = list(richterOutput)
        richterOutputConcat = richterOutput + strings
        # richterOutputConcat = str(richterOutputConcat)

        print(richterOutputConcat)
        outfile = open('earthquakesChristopherOsborne.txt', 'w')
        # richterOutput = list(richterOutput)
        # print(richterOutput)
        # for item in richterOutput:
        #     richterOutput = list(item)
            # outfile.write(item + '\n')
        # richterOutput = str(richterOutput)
        # print(richterOutput)
        outfile.write(str(richterOutputConcat))
        # outfile.write('\n'.join(richterOutput))
        # outfile.write('\t'.join(conversions))
        outfile.close()
    except IOError:
        print('An error occurred trying to read the input file. Please try again!')

# 1 All the other things get carried over from the previous lab except calculating and writing the table
# 2 Read the values from the richters.txt file into a list using the readlines() method
# 3 Sort the list using the sort method for example mylist.sort()
# 4 Create a new list using for example newlist = []
# 5 append all the values you read from the file into newlist
# 6 then in a loop for example for value in newlist:
# 7 read each value; calculate the joules and TNT; and write it to the output file
def richterValues(strings):
    try:
        infile = open('richters.txt', 'r')
        richterValues = infile.readlines()
        infile.close()

        # create a loop that iterates through the list to make them floats.
        i = 0
        while i < len(richterValues):
            richterValues[i] = float(richterValues[i].rstrip('\n'))
            i += 1

        richterValues = sorted(richterValues)


    except IOError:
        print('An error occurred trying to read the input file. Please try again!')

def greetingMessage():
    # Greeting message to user
    print('     Rumble     Rumble     Rumble')
    print('I think we just felt an earthquake!')
    print(' ')

def inputRichter():
    try:
        richterScale = float(input('How big do you think that was on the Richter Scale? (Usually a Richter Scale is measured from 1-10) '))
        return richterScale
    except ValueError:
        print('Error! Please input a number and not the literal saying of a number.')

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
